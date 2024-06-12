import streamlit as st
import serial
#b'$GPGLL,2628.53446,N,07307.01364,E,170518.00,A,A*6E\r\n'

# Example Python code to create a Google Maps link from NEO-6M GPS output

# Example GPS output
gps_output = "$GPGLL,2628.75146,N,07306.9864,E,060641.00,A,A*6E"

# Parse GPS output to extract latitude and longitude
def parse_gps_output(gps_output):
    data = gps_output.split(',')
    if data[0] == "$GPGLL":
        latitude = float(data[1][:2]) + float(data[1][2:]) / 60
        if data[2] == 'S':
            latitude = -latitude
        longitude = float(data[3][:3]) + float(data[3][3:]) / 60
        if data[4] == 'W':
            longitude = -longitude
        return latitude, longitude
    else:
        return None, None

# Format coordinates into decimal degrees
def format_coordinates(latitude, longitude):
    return f"{latitude:.6f},{longitude:.6f}"

# Create Google Maps link
def create_google_maps_link(latitude, longitude):
    return f"https://www.google.com/maps?q={latitude},{longitude}"

# Function to send command to Arduino to extend the actuator
def extend_actuator(ser):
    ser.write(b'1')  # Send '1' to Arduino to extend actuator
    st.write("Extending the actuator...")

# Function to send command to Arduino to retract the actuator
def retract_actuator(ser):
    ser.write(b'0')  # Send '0' to Arduino to retract actuator
    st.write("Retracting the actuator...")

# Main function
def main():
    ser = serial.Serial('COM5', 115200)
    st. title("arduino extend/retract")
        # Button to extend the actuator
    if st.button("Extend"):
        extend_actuator(ser)

    # Button to retract the actuator
    if st.button("Retract"):
        retract_actuator(ser)

    st.title("Serial Data Viewer")

    if st.button("Read Data"):
        while True:
            #ser.write(b'2')  # Send '2' to arduino for gps access
            #gps_output = ser.readline()
            #gps_output = gps_output.decode('utf-8')
            st.write(gps_output)
            latitude, longitude = parse_gps_output(gps_output)
            if latitude is not None and longitude is not None:
                formatted_coordinates = format_coordinates(latitude, longitude)
                google_maps_link = create_google_maps_link(latitude, longitude)
                st.sidebar.write("Formatted Coordinates:", formatted_coordinates)
                st.sidebar.write("Google Maps Link:", google_maps_link)
            else:
                print("Invalid GPS output or unsupported sentence.")

if __name__ == "__main__":
        main()
#$GPGLL,2628.52221,N,07307.02281,E,060641.00,A,A*6E
