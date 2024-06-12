'''import serial
import streamlit as st
ser1 = serial.Serial('COM9',9600)
while True:
    line = ser1.readline()
    st.write(line)
    '''
import serial
import streamlit as st

def main():
    ser = serial.Serial('COM12', 115200)

    st.title("Serial Data Viewer")

    if st.button("Read Data"):
        while True:
            line = ser.readline()
            st.write(line)

if __name__ == "__main__":
    main()
