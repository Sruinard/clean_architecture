#!/bin/bash

# DECLARE
## general
RESOURCE_GROUP="clean_architecture_setup"
LOCATION="westeurope"

## cosmos
COSMOS_DB_ACCOUNT="cabrenterdb${RANDOM}"

## sql
server="sql-server-${RANDOM}"
database="sql-database-${RANDOM}"
login="sampleLogin"
password="samplePassword123!"
startIP=0.0.0.0
endIP=255.255.255.255

## webapp
WEBAPP_PLAN="cleanarchitecturewebapp${RANDOM}"
WEBAPP="wawebappdemo${RANDOM}"

#BUILD
# Configure defaults values
az configure --scope local --defaults group=$RESOURCE_GROUP location=$LOCATION 

# create resource group
az group create --resource-group $RESOURCE_GROUP -l $LOCATION
echo "Resource group created"

# create cosmosdb account
echo "Creating cosmos account ${COSMOS_DB_ACCOUNT}"
az cosmosdb create --name $COSMOS_DB_ACCOUNT --kind MongoDB
az cosmosdb mongodb database create --account-name  ${COSMOS_DB_ACCOUNT} --name cabcenter


# create SQLserver + database
echo "Creating $server"
az sql server create --name $server --admin-user $login --admin-password $password

echo "Configuring firewall..."
az sql server firewall-rule create --server $server -n AllowYourIp --start-ip-address $startIP --end-ip-address $endIP

echo "Creating $database on $server..."
az sql db create --server $server --name $database --edition GeneralPurpose --family 'Gen5' --capacity 2 --zone-redundant false # zone redundancy is only supported on premium and business critical service tiers


# create static webapp
az appservice plan create --name $WEBAPP_PLAN --sku B1 --is-linux
az webapp create --name $WEBAPP  --plan $WEBAPP_PLAN --runtime 'python|3.6'
az webapp cors add  -n $WEBAPP --allowed-origins '*'
az webapp config set -n $WEBAPP --startup-file 'gunicorn -w 2 -k uvicorn.workers.UvicornWorker cabrenter.main:app'

CONNECTION_STRING=$(az cosmosdb keys list --name ${COSMOS_DB_ACCOUNT} --type connection-strings --query 'connectionStrings[0].connectionString')
az webapp config appsettings set --settings CONNECTION_STRING=$CONNECTION_STRING SQL_ADMIN=$login SQL_PASSWORD=$password SQL_DATABASE=$database SQL_SERVER="${server}.database.windows.net"  --name $WEBAPP

cd ./backend && az webapp up -n $WEBAPP && cd ..
