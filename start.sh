echo "Cloning Repo...."

if [ -z "$BRANCH" ]
then
  echo "Cloning main branch...."
  git clone https://github.com/anujedits42-byte/Ultra-Forward-Botss
else
  echo "Cloning $BRANCH branch...."
  git clone -b $BRANCH https://github.com/anujedits42-byte/Ultra-Forward-Botss
fi

cd Ultra-Forward-Botss

pip3 install -U -r requirements.txt

echo "Starting Bot...."
python3 bot.py
