# Custom Message & Service Definitions in ROS2

A beginner ROS2 project demonstrating how to create **custom message (.msg)** and **service (.srv)** definitions and use them with Python client-server communication.

## Project Overview

This project focuses on understanding how ROS2 communication works using **IDL-defined interfaces**. It includes:

- Custom message definition (`RobotStatus.msg`)
- Custom service definition (`SetMode.srv`)
- Python service server
- Python service client
- Interface generation using `rosidl_default_generators`

The goal is to understand that ROS2 interfaces are **language-independent communication contracts**.

---

## Project Structure

```text
second_project/
│── src/
│   ├── ros_interface/
│   │   ├── msg/
│   │   │   └── RobotStatus.msg
│   │   ├── srv/
│   │   │   └── SetMode.srv
│   │
│   ├── robot_controller/
│   │   ├── robot_controller/
│   │   │   ├── set_mode_server.py
│   │   │   └── set_mode_client.py
│
│── screenshots/
│── README.md
```

---

## Custom Message Definition

### RobotStatus.msg

```text
string name
float32 battery
bool is_active
```

### Purpose

Used to represent robot state information:

- Robot name
- Battery percentage
- Active status

---

## Custom Service Definition

### SetMode.srv

```text
string mode
---
bool success
string message
```

### Purpose

Allows changing robot operating mode.

### Request

- `mode` → AUTO / MANUAL

### Response

- `success` → True or False
- `message` → Response status

---

## Installation & Build

Clone repository:

```bash
git clone git@github.com:bhushanpatil25-oss/Custom-Message-Service-Definitions-in-ros2.git
```

Go to workspace:

```bash
cd second_project
```

Build workspace:

```bash
colcon build
```

Source setup:

```bash
source install/setup.bash
```

---

## Running the Project

### Run Server

```bash
ros2 run robot_controller server
```

Expected output:

```text
Requested mode: AUTO
```

### Run Client

Open another terminal:

```bash
source install/setup.bash
ros2 run robot_controller client
```

Expected output:

```text
True
Mode changed
```

---

## Screenshots

### Server Output

![Server Output](screenshots/server_output.png)

### Client Output

![Client Output](screenshots/client_output.png)

---

## Concepts Learned

- ROS2 Interface Definition Language (IDL)
- Custom `.msg` files
- Custom `.srv` files
- Service request-response communication
- `rosidl_default_generators`
- ROS2 package dependencies
- Python ROS2 nodes

---

## Author

**Bhushan Patil**  
ROS2 Learning Project
