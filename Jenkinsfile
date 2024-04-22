pipeline {
    agent any
    stages {
        stage("build"){
            steps{
               sh 'docker login -u siddharthtewari -p  c2lkZGhhcnRodGV3YXJpOmRja3JfcGF0X2RGRm9zc1JCdndnTWlSMXpwQWU2OEVWejhMSQ=='
               sh 'docker build ./userhandle/ -t  siddharthtewari/cc_user'
               sh 'docker push siddharthtewari/cc_user'
               sh 'docker build ./products/ -t siddharthtewari/cc_product'
               sh 'docker push siddharthtewari/cc_product'
               sh 'docker build ./orders/ -t siddharthtewari/cc_orders'
               sh 'docker push siddharthtewari/orders'
            }
        }

        stage("deploy"){
            steps{
            //Assuming minikube to be running
               sh 'kubectl apply -f ./User/user_deployment.yaml'
               sh 'kubectl rollout restart deployment userhandle'

               sh 'kubectl apply -f ./Products/products_deployment.yaml'
               sh 'kubectl rollout restart deployment products'

               sh 'kubectl apply -f ./Orders/order_deployment.yaml'
               sh 'kubectl rollout restart deployment orders'

               sh 'kubectl apply -f ingress.yaml'
            }
        }
    }
    post{
      failure{
         echo "Pipeline failed"
      }
    }
}
