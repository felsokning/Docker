In order to build/run this, you will need to ensure that you're targeting Python3. All of the files should be set-up for this and this builds locally on an Ubuntu machine (Swedish locale) but, just in case, if you can't get it to work, it's most probably because of Unicode --> ASCII.

Build via Docker (from within the SwedishWeekNumber folder):
sudo docker build -t koddebugging/svenskaveckannummer .

Run locally:
sudo docker run -d -p 4000:80 koddebugging/svenskaveckannummer
