rm -r build
rm -r dist
find gdm/ -type d -name "__pycache__" | xargs rm -r
rm *.spec