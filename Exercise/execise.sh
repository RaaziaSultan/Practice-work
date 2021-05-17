
#! /bin/bash
FILE=$1
if [ -z "$FILE" ]; then
   echo "File $FILE name is Empty"
   exit 1
fi
if [ $# -ne 1 ]; then
   echo "Invalid argument"
   exit 1
fi
if [ ! -w $fILE ]; then
   echo "No write permission"
elif [ ! -r $file ]; then
   echo "No read permission"
   exit 1
fi
if [ -s "$FILE" ]; then
   echo "File $FILE is not empty and exists"
   counter=$(cat $FILE  | cut -d' ' -f3)
   counter=$(($counter+1))
echo "counter = $counter"> $FILE
else
   echo "File $FILE is empty and does not exist"
   echo "counter = 1"> $FILE
fi
