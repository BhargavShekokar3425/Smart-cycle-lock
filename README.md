
# Smart Cycle Lock Streamlit Application

This project is a Streamlit application that interfaces with an Arduino through a serial connection. It provides functionalities to extend and retract an actuator and read GPS data, parse it, and display a Google Maps link for the current GPS coordinates.

## Overview

### Features
- **Actuator Control**: Extend and retract the actuator using the application interface.
- **GPS Data Viewer**: Read GPS data, parse it, and display formatted coordinates along with a Google Maps link.

## Requirements

- Python 3.x
- Streamlit
- pyserial

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install the required packages:
   ```sh
   pip install streamlit pyserial
   ```

## Running the Application

1. Connect your Arduino to the computer.
2. Run the Streamlit application:
   ```sh
   streamlit run app.py
   ```

## Application Usage

### Actuator Control
- **Extend Actuator**: Click the "Extend" button to send a command to the Arduino to extend the actuator.
- **Retract Actuator**: Click the "Retract" button to send a command to the Arduino to retract the actuator.

### GPS Data Viewer
- **Read Data**: Click the "Read Data" button to read GPS data from the serial connection. The application will parse the GPS data and display:
  - Formatted coordinates in decimal degrees.
  - A Google Maps link pointing to the current GPS location.

## Code Explanation

### Main Functions
- `parse_gps_output(gps_output)`: Parses the GPS output string to extract latitude and longitude, converting coordinates into decimal degrees.
- `format_coordinates(latitude, longitude)`: Formats the parsed latitude and longitude into a string with six decimal places.
- `create_google_maps_link(latitude, longitude)`: Creates a Google Maps link using the latitude and longitude.
- `extend_actuator(ser)`: Sends a command to the Arduino to extend the actuator.
- `retract_actuator(ser)`: Sends a command to the Arduino to retract the actuator.

### Main Application Flow
1. **Setup Serial Connection**:
   ```python
   ser = serial.Serial('COM5', 115200)  # Initializes the serial connection to the Arduino.
   ```
2. **Streamlit Interface**:
   - Title for the actuator control section.
   - Buttons for extending and retracting the actuator.
   - Title for the serial data viewer.
   - Button for reading data from the serial connection.
3. **GPS Data Handling**:
   - Reads GPS data from the serial connection.
   - Parses and formats the GPS data.
   - Displays the formatted coordinates and Google Maps link in the Streamlit sidebar.

## Example Usage

### Example GPS Output
```sh
$GPGLL,2628.75146,N,07306.9864,E,060641.00,A,A*6E
```

### Parsed Coordinates
- **Latitude**: 26.479191
- **Longitude**: 73.116440

### Google Maps Link
```sh
https://www.google.com/maps?q=26.479191,73.116440
```

## Notes
- Make sure the Arduino is connected to the correct COM port specified in the code ('COM5' in the example).
- Ensure the baud rate matches the settings on your Arduino (115200 in the example). You can adjust the COM port and baud rate in the code as needed.

## Troubleshooting

### Serial Connection Issues:
- Verify the correct COM port is used.
- Ensure no other applications are using the same COM port.

### Data Parsing Issues:
- Check if the GPS module is providing the correct NMEA sentences (e.g., `$GPGLL` in this case).

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
