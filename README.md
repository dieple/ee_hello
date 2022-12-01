# Note

A simple hello world to demonstrate it can be deployed on minukube and load balanced.

# Build
```bash
#docker build -t hello_world:1.0.1 .
minikube image build -t hello_world:1.0.1 .
```

# Deploy on minikube
```bash
minikube start

kubectl create deployment balanced --image=hello_world:1.0.1
kubectl get deploy
NAME       READY   UP-TO-DATE   AVAILABLE   AGE
balanced   1/1     1            1           8s


kubectl expose deployment balanced --type=LoadBalancer --port=80
service/balanced exposed

kubectl get svc
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
balanced     LoadBalancer   10.108.217.196   <pending>     80:31135/TCP   26s
kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP        111m
```


In another window, start the tunnel to create a routable IP for the ‘balanced’ deployment:

```bash
minikube tunnel
```

To find the routable IP, run this command and examine the EXTERNAL-IP column:

```bash
kubectl get services balanced
NAME       TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
balanced   LoadBalancer   10.108.217.196   127.0.0.1     80:31135/TCP   92s

```
Your deployment is now available at "EXTERNAL-IP":80