#!/bin/bash

# Verifica se o número de argumentos está correto
if [ "$#" -ne 1 ]; then
    echo "Uso: $0 <URL>"
    exit 1
fi

# Faz o request usando curl e pega o cabeçalho HTTP
header=$(curl -sI "$1")

# Extrai a linha contendo a localização do redirecionamento
location=$(echo "$header" | grep -i '^location:' | tr -d '\r')

# Extrai apenas a URL do redirecionamento usando cut
redirect_url=$(echo "$location" | cut -d' ' -f2)

echo "Endereço real do link: $redirect_url"
