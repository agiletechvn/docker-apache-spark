# IMAGE=$1
echo "Building spark image..."
docker build -f spark.df -t $IMAGE .
echo