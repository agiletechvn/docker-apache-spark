IMAGE=$1
: ${IMAGE:=thanhtu/spark}
# PUBLIC_DNS=$(ifconfig | awk '/inet /{print $2}' | grep -v 127.0.0.1 | tail -1)
PUBLIC_DNS=127.0.0.1
IMAGE_CHECK=$(docker images | grep $IMAGE)

if [[ -z $IMAGE_CHECK ]];then
  ./build.sh
fi
echo "Starting spark network: IMAGE: $IMAGE, PUBLIC_DNS: $PUBLIC_DNS ..."
PUBLIC_DNS=$PUBLIC_DNS IMAGE=$IMAGE docker-compose up -d
echo "Done."
