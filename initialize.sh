#!/bin/bash -

sudo apt-get update
sudo apt-get install unzip

./config/environment/setup.sh

source ~/pyvirenvs/match_and_write/bin/activate

pip install -r config/dependencies/install.txt

PROJECT_PATH=`pwd`

cat <<EOF >$PROJECT_PATH/activate.sh
#!/bin/bash -i

source ~/pyvirenvs/match_and_write/bin/activate
./config/dependencies/install.sh
EOF

chmod 777 activate.sh