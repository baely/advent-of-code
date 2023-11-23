# Read year and day number from args
YEAR=$1
DAY=$2

mkdir ./$YEAR
mkdir ./$YEAR/$DAY

cp -n ./template/* ./$YEAR/$DAY