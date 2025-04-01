#!/bin/bash

# Script para aplicar el deployment de Redis en Kubernetes

# Aplicar el archivo de configuración de Kubernetes
kubectl apply -f ./headless-redis.yaml

# Aplicar el archivo de configuración de Kubernetes
kubectl apply -f ./statefulset-redis.yaml

# Verificar si el deployment se ha creado correctamente
kubectl get pods -l app=redis