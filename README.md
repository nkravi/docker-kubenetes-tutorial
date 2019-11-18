# Docker kubernetes Tutorial

### Step 1 Configure git 
- install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Type this on terminal `git clone git@github.com:nkravi/docker-kubenetes-tutorial.git`
- This should download a new folder named `docker-kubenetes-tutorial`

### Step 2 Setup docker
- install docker - for [windows](https://docs.docker.com/docker-for-windows/install/) / for [mac](https://docs.docker.com/docker-for-mac/install/)
- create a dockerhub [account](https://hub.docker.com/)

### Step 3 Dockerize app
- Go to `docker-kubenetes-tutorial\hello_app`
- Build docker `docker build -t {your_dockerhub_name}/helloapp .`
- See if image is built properly `docker images`
- Go to `docker-kubenetes-tutorial\hola_app`
- Build docker `docker build -t {your_dockerhub_name}/holaapp .`
- See if image is built properly `docker images`
- push docker images to dockerhub `docker push {your_dockerhub_name}/helloapp` and `docker push {your_dockerhub_name}/holaapp`

### Step 4 Run app locally
- Start hello app `docker run -p 5000:5000 {your_dockerhub_name}/helloapp`
- Start hola app `docker run -p 5001:5001 {your_dockerhub_name}/holaapp`
- hit `http://localhost:5000/nkravi` - you should see hello nkravi
- hit `http://localhost:5001/nkravi` - you should see hola nkravi

### Step 5 run it on kubernetes
- Go to [kubernetes](https://kubernetes.io/docs/tutorials/hello-minikube/#create-a-minikube-cluster)
- Click on `launch terminal` button. Give it a minute. This will start minikube cluster
- After cluster started click on `preview port` , This should open a new tab
- Click on `create button` on top right corner
- Copy paste yaml files from `docker-kubenetes-tutorial/kubernetes` one by one and click on upload 
- Now you should see `2 services` , `2 deployments` and `1 ingress` running 
- Play with it

### Furter Readings
- [Docker Tutorial](https://docs.docker.com/get-started/)
- [Kubernetes Tutorial](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
