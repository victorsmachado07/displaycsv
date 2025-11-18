#!/usr/bin/env bash
set -e

RESOURCE_GROUP="rg-gs-cloud"
LOCATION="brazilsouth"
PLAN_NAME="plan-gs-cloud"
APP_NAME="webapp-gs-cloud"
SKU="B1"

echo ">> Criando Resource Group..."
az group create --name $RESOURCE_GROUP --location $LOCATION

echo ">> Criando App Service Plan..."
az appservice plan create \
    --name $PLAN_NAME \
    --resource-group $RESOURCE_GROUP \
    --sku $SKU \
    --is-linux

echo ">> Criando WebApp (Python 3.12)..."
az webapp create \
    --name $APP_NAME \
    --resource-group $RESOURCE_GROUP \
    --plan $PLAN_NAME \
    --runtime "python|3.12"

echo ">> Ativando SCM_DO_BUILD_DURING_DEPLOYMENT..."
az webapp config appsettings set \
    --resource-group $RESOURCE_GROUP \
    --name $APP_NAME \
    --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true

echo "===== INFRA CRIADA COM SUCESSO ====="
echo "URL: https://$APP_NAME.azurewebsites.net"
