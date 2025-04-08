#!/bin/bash

# Script para matar todos los Services
kubectl delete service public-service-coordinador
kubectl delete service public-service-poolmanager
kubectl delete service public-service-rabbitmq
kubectl delete service service-coordinador
kubectl delete service service-poolmanager
kubectl delete service service-rabbitmq
kubectl delete service service-redis
kubectl delete service service-worker