kubectl apply -f ./User/user_deployment.yaml
kubectl rollout restart deployment userhandle

kubectl apply -f ./Products/product_deployment.yaml
kubectl rollout restart deployment products

kubectl apply -f ./Orders/orders_deployment.yaml
kubectl rollout restart deployment orders

kubectl apply -f ingress.yaml
