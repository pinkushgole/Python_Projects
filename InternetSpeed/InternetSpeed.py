
import speedtest



import speedtest

# Create a Speedtest object
st = speedtest.Speedtest()

# Fetch the list of servers (this can take a little time)
st.get_best_server()

# Perform download and upload speed tests
download_speed = st.download() / 1_000_000  # Convert from bits to Mbps
upload_speed = st.upload() / 1_000_000      # Convert from bits to Mbps

# Ping (latency)
ping = st.results.ping

print(f"Download speed: {download_speed:.2f} Mbps")
print(f"Upload speed: {upload_speed:.2f} Mbps")
print(f"Ping: {ping} ms")