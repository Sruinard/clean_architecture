#!/bin/bash

# declare variables
RESOURCE_GROUP="clean_architecture_setup"
LOCATION="westeurope"
COSMOS_DB_ACCOUNT="cabrenterdb${RANDOM}"

server="sql-server-${RANDOM}"
database="sql-database-${RANDOM}"

login="sampleLogin"
password="samplePassword123!"

startIP=0.0.0.0
endIP=0.0.0.0

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
az sql db create --server $server --name $database --edition GeneralPurpose --family Gen5 --capacity 1 --zone-redundant false # zone redundancy is only supported on premium and business critical service tiers
