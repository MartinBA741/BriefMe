## Local deployment
cd "C:\Users\MartinBirkAndreasen\Desktop\Jazz\sum_app"
sudo docker build -t summerizerapp .
sudo docker run -p 80:80 summerizerapp

--> GO TO: http://localhost:80

## wsl
cd /mnt/c/Users/MartinBirkAndreasen/Desktop/Jazz/sum_app/

## Docker
sudo docker ps
sudo docker container ls
sudo docker build -t summerizerapp .
sudo docker run -p 80 summerizerapp


## Docker Hub
docker login
docker tag summerizerapp martinba741/academy:summerizerapp
docker push martinba741/academy:summerizerapp


-- now remove local v1 image:
docker rmi summerizerapp


-- Now we can run docker image from azure registry (locally)
docker run martinba741/academy:summerizerapp


### Run container in Azure
az login
docker login

# cpu
az container create --resource-group rg-academy --name sumcontainer --image martinba741/academy:summerizerapp --dns-name-label sum-demo --ports 80

# gpu
az container create --resource-group rg-academy --file sku-gpu.yaml

az container logs   --resource-group rg-academy --name gpucontainergroup --container-name summerizergpucontainer
az container delete --resource-group rg-academy --name gpucontainergroup --container-name summerizergpucontainer -y

# show
az container show   --resource-group rg-academy --name sumcontainer --query "{FQDN:ipAddress.fqdn,ProvisioningState:provisioningState}" --out table
az container logs   --resource-group rg-academy --name sumcontainer

az container delete --resource-group rg-academy --name sumcontainer
az container list --resource-group rg-academy --output table