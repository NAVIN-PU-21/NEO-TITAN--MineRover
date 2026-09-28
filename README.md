# NEO TITANS — SIH Software Demo

**Smart India Hackathon 2026 — SIH26039**  
**AI-Powered Underground Mine Safety, Monitoring and Rescue System**

A simple Streamlit demonstration dashboard for the NEO TITAN 1 rover.

## Demo login
- Username: `admin`
- Password: `neotitans2026`

## What the jury can see
Login → live-looking sensor telemetry → SAFE/WARNING/CRITICAL risk → rover map → hazard panel → AI vision placeholder → rover controls → software module status.

The dashboard is intentionally self-contained and uses simulated values so it can be demonstrated without the physical rover.

## Project software stack
Python, OpenCV + YOLOv8, AI/ML + sensor fusion, A*/Dijkstra path planning, SLAM/RTAB-Map, Streamlit, with Raspberry Pi 4B and LoRa planned for edge/communication integration.

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Repository structure
```text
neo-titans-sih-software/
├── app.py
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── auth.py
│   └── dashboard.py
├── data/
│   └── sample_sensor_data.json
└── .streamlit/
    └── config.toml
```

## Development roadmap
1. Dashboard and demo login
2. Raspberry Pi sensor/GPIO integration
3. Real LoRa telemetry
4. OpenCV + YOLOv8 camera pipeline
5. AI multi-factor risk assessment
6. A*/Dijkstra route planning
7. SLAM/RTAB-Map mapping
8. Hardware testing and validation

> Demo software only. Do not use simulated values for real mine-safety decisions.
