#!/bin/bash

# Script para aplicar el deployment de RabbitMQ en Kubernetes

# Aplicar el archivo de configuración de Kubernetes
kubectl apply -f ./headless-rabbitmq.yaml

# Aplicar el archivo de configuración de Kubernetes
kubectl apply -f ./statefulset-rabbitmq.yaml

# Aplicar el archivo de configuración de Kubernetes
#kubectl apply -f ./service-rabbitmq.yaml