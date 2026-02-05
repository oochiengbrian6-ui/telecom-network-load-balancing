# telecom-network-load-balancing
# Telecom Network Load Balancing Simulation

## Overview
This project analyzes a distributed telecom network dataset to identify
latency bottlenecks and implement a Python-based load balancing strategy
for optimal CPU and memory utilization.

## Assignment Objectives
The objectives of this assignment are:
1. To identify the node causing maximum latency in the network
2. To propose a process allocation strategy for load balancing
3. To simulate load redistribution using Python

## Dataset Description
The dataset represents multiple telecom nodes with the following parameters:
- Latency (milliseconds)
- Throughput (Mbps)
- Packet Loss (%)
- CPU Utilization (%)
- Memory Usage (GB)
- Hosted Services

## Part (a): Latency Analysis
The latency analysis identifies the node with the highest delay using
Python data processing. Results show that **CloudZ** has the highest
latency (22 ms), largely due to high CPU utilization and analytics workloads.

## Part (b): Process Allocation Strategy
To balance the network load:
- CPU-intensive services are moved from overloaded nodes
- Underutilized edge and core nodes receive redistributed load
- Both CPU and memory utilization are considered during allocation

This strategy reduces performance bottlenecks while maintaining service availability.

## Part (c): Load Balancing Simulation
A Python-based simulation dynamically redistributes CPU and memory load
from overloaded nodes to nodes with lower utilization. The simulation
outputs show improved balance after redistribution.

## Project Structure
