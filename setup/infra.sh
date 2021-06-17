#!/bin/bash

# DECLARE
## general
RESOURCE_GROUP="clean_architecture_setup"
LOCATION="westeurope"

## cosmos
COSMOS_DB_ACCOUNT="cabrenterdb${RANDOM}"

## sql
SERVER="sql-server-${RANDOM}"
DATABASE="sql-database-${RANDOM}"
LOGIN="sampleLogin"
PASSWORD="samplePassword123!"
START_IP=0.0.0.0
END_IP=255.255.255.255

## webapp
WEBAPP_PLAN="cleanarchitecturewebapp${RANDOM}"
WEBAPP="cawebappdemo${RANDOM}"

#BUILD
# Configure defaults values
az configure --scope local --defaults group=$RESOURCE_GROUP location=$LOCATION 

# create resource group
az group create --resource-group $RESOURCE_GROUP -l $LOCATION
echo "Resource group created"

# create cosmosdb account
echo "Creating cosmos account $COSMOS_DB_ACCOUNT"
az cosmosdb create --name $COSMOS_DB_ACCOUNT --kind MongoDB
az cosmosdb mongodb database create --account-name  $COSMOS_DB_ACCOUNT --name cabcenter


# create SQLserver + database
echo "Creating $SERVER"
az sql server create --name $SERVER --admin-user $LOGIN --admin-password $PASSWORD

echo "Configuring firewall..."
az sql server firewall-rule create --server $SERVER -n AllowYourIp --start-ip-address $START_IP --end-ip-address $END_IP

echo "Creating $DATABASE on $SERVER..."
az sql db create --server $SERVER --name $DATABASE --edition GeneralPurpose --family 'Gen5' --capacity 2 --zone-redundant false # zone redundancy is only supported on premium and business critical service tiers


# create static webapp
az appservice plan create --name $WEBAPP_PLAN --sku B1 --is-linux
az webapp create --name $WEBAPP  --plan $WEBAPP_PLAN --runtime 'python|3.6'
az webapp cors add  -n $WEBAPP --allowed-origins '*'
az webapp config set -n $WEBAPP --startup-file 'gunicorn -w 2 -k uvicorn.workers.UvicornWorker cabrenter.main:app'

CONNECTION_STRING=$(az cosmosdb keys list --name ${COSMOS_DB_ACCOUNT} --resource-group ${RESOURCE_GROUP} --type connection-strings --query "connectionStrings[0].connectionString" | tr -d \")
az webapp config appsettings set --settings CONNECTION_STRING=$CONNECTION_STRING SQL_ADMIN=$LOGIN SQL_PASSWORD=$PASSWORD SQL_DATABASE=$DATABASE SQL_SERVER="${SERVER}.database.windows.net"  --name $WEBAPP

cd ./backend && az webapp up -n $WEBAPP && cd ..

