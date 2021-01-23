#!/bin/bash

echo "-------------------------------------------------------------------------"
if ( [[ "${1}" = "uninstall" ]] ); then
    echo "INFO: Removing Marvel API installation from namespace marvelapi"
    kubectl config set-context --current --namespace=marvelapi
    kubectl delete -f deployment.yaml
    kubectl delete -f namespace.yaml
else
	echo "INFO: Installing Marvel API in marvelapi namespace"
    kubectl config set-context --current --namespace=marvelapi
    kubectl apply -f namespace.yaml
    kubectl apply -f deployment.yaml
    sleep 30
    kubectl get all
fi
echo "-------------------------------------------------------------------------"
echo "Finished"