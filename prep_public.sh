if [ -d "./public/*" ]; then
    rm -r ./public/*
    echo "Removed all files and directories in public/"
fi
cp -a ./static/* ./public/