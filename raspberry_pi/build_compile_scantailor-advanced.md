sudo apt get-update
sudo apt-get upgrade

sudo apt install build-essential cmake qt5-qmake qtbase5-dev libqt5opengl5-dev libtiff5-dev libjpeg-dev libpng-dev libqt5svg5-dev libboost-test-dev git

cd ~
git clone https://github.com/4lex4/scantailor-advanced.git
cd scantailor-advanced


mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j1
sudo make install