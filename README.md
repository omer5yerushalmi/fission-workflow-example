# Argo Workflow, Argo Events and Fission Example

This example project demonstrates the integration of Argo Events, Argo Workflow, and Fission to create an event-driven serverless workflow. In this scenario, a Python script publishes a message to RabbitMQ, and Argo Events automatically triggers an Argo Workflow that executes a Fission function.

## Prerequisites

Before you begin, ensure that you have the following installed and configured:

- Kubernetes cluster
- Argo Events
- Argo Workflows
- Fission

## Project Structure

The project consists of the following components:

1. **RabbitMQ Setup (`rabbitmq-setup.yaml`):**
   YAML file sets up a RabbitMQ cluster with specific configurations.
   
2. **Python Script (`rabbitmq-publisher.py`):**
   A Python script that publishes a message to a RabbitMQ queue.
   
2. **Python Function (`hello.py`):**
   A simple python function.

3. **Argo Workflow (`fission-python-workflow.yaml`):**
   A stand-alone Argo Workflow. It deploys and runs a Fission function.

4. **Argo Events (`sensor.yaml`, `event-source.yaml`, `sensor-rbac.yaml`):**
   Argo Events configuration files defining a sensor that listens for RabbitMQ events and triggers the Argo Workflow.

## Setup

1. **Clone the Repository:**
   ```
   git clone https://github.com/omer5yerushalmi/fission-workflow-example.git
   cd fission-workflow-example
   ```
2. **Set up RabbitMQ:**
   ```
   kubectl apply -n default -f rabbitmq/rabbitmq-setup.yaml
   ```
3. **Expose the RabbitMQ server to local publisher using port-forward:**
   ```
   kubectl -n default port-forward <rabbitmq-pod-name> 5672:5672
   ```
4. **Create the event source:**
   ```
   kubectl apply -n argo-events -f argo-events/event-source.yaml
   ```
5. **Create and configure the sensor:**
   ```
   kubectl apply -n argo-events -f argo-events/sensor.yaml
   kubectl apply -n argo-events -f argo-events/sensor-rbac.yaml
   ```
6. **Open a python REPL and run following code to publish a message:**
   ```
   python rabbitmq/rabbitmq-publisher.py
   ```
7. **As soon as you publish a message, sensor will trigger an Argo workflow. Run argo list to find the workflow.**
