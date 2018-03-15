PUBLIC_DNS=$(ifconfig | awk '/inet /{print $2}' | grep -v 127.0.0.1 | tail -1)
IMAGE_CHECK=$(docker images | grep spark)

if [[ -z $IMAGE_CHECK ]];then
  ./build.sh
fi
echo "Starting spark network, PUBLIC_DNS: $PUBLIC_DNS ..."
PUBLIC_DNS=$PUBLIC_DNS docker-compose up -d
echo "Done."