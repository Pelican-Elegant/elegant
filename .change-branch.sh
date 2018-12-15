#!/bin/bash
echo "Changing branch to 'next'"
sed -i "s/rev: master/rev: next/g" peru.yaml
