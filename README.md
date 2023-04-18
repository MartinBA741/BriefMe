# Deployment
## Local deployment with streamlit
streamlit run app.py


## Local deployment with docker
sudo docker build -t summerizerapp .
sudo docker run -p 80:80 summerizerapp

--> GO TO: http://localhost:80

sudo docker stop summerizerapp



## Deploy container in Azure
az login
docker login

### cpu
az container create --resource-group rg-academy --name sumcontainer --image martinba741/academy:summerizerapp --dns-name-label sum-demo --ports 80

### gpu
az container create --resource-group rg-academy --file infrastructure\sku-gpu.yaml

az container logs   --resource-group rg-academy --name gpucontainergroup --container-name summerizergpucontainer
az container delete --resource-group rg-academy --name gpucontainergroup --container-name summerizergpucontainer -y

### show
az container show   --resource-group rg-academy --name sumcontainer --query "{FQDN:ipAddress.fqdn,ProvisioningState:provisioningState}" --out table
az container logs   --resource-group rg-academy --name sumcontainer

az container delete --resource-group rg-academy --name sumcontainer
az container list --resource-group rg-academy --output table