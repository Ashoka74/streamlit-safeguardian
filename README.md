<div align="center">

  <img src="https://github.com/user-attachments/assets/02d63c35-98fb-4537-82df-8d373d0d47f1" width="200px" />

  <h1 style="border-bottom: none;">SafeGuardianAI</h1>

  <p><em>Decentralized AI-Driven Disaster Response Assistant</em></p>

  <a href="https://x.com/nexa_ai/status/1828490311426846865">
    <img src="https://img.shields.io/badge/1st%20Prize%20at%20SuperAgentAI%20Hackathon%20-%20Stanford%20ResearchPark-yellow" alt="1st Prize at SuperAgentAI Hackathon" />
  </a>

  <a href="https://opensource.org/licenses/gpl-3-0"><img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="License: GPL 3.0"/></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+"/></a>
  <a href="https://huggingface.co/organizations/SafeGuardianAI/share/kenFDVCMqdyHJYwsMwxWivXcwFqXBAAsHr">
<img alt="Spaces" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue">
</a>
  <a href="https://safeguardian-llm.streamlit.app/"><img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Streamlit App"/></a>
</div>

<h2>🌟 Overview</h2>

<p><b>SafeGuardianAI</b> is an innovative emergency response platform that harnesses the power of artificial intelligence to provide critical support during catastrophic events. By seamlessly integrating real-time data analysis, offline capabilities, and community-driven support, SafeGuardianAI bridges the gap between individuals, communities, and emergency services, ensuring a more coordinated and effective response to disasters.</p>

https://github.com/user-attachments/assets/e40dd7bf-9a91-4acd-9985-7910789c3e91


<h2>🚀 Key Features</h2><ul>
  
  <li>💬 <strong>AI-Powered Chat Interface</strong>: Interact with GuardianAI for personalized emergency assistance and real-time guidance.</li>
  <li>🎙️ <strong>Multi-Modal Activation</strong>: Trigger emergency mode via text, voice commands, or automatic motion detection for hands-free operation.</li>
  <li>👤 <strong>Smart User Profiles</strong>: Store vital information securely for quick access during emergencies, including medical history and emergency contacts.</li>
  <li>📱 <strong>Offline Functionality</strong>: Access critical guides and emergency procedures without an internet connection, ensuring help is always available.</li>
  <li>🧠 <strong>Real-time Situation Assessment</strong>: Receive tailored responses and advice based on AI analysis of current conditions and user input.</li>
  <li>🤝 <strong>Community Coordination</strong>: Facilitate local collaboration during large-scale events, connecting neighbors and organizing grassroots relief efforts.</li>
  <li>🗺️ <strong>Resource Management</strong>: Locate and manage emergency services, shelters, and supplies with an interactive, real-time updated map.</li>
  <li>📊 <strong>Data-Driven Insights</strong>: Collect anonymous data to improve future disaster responses and enhance predictive capabilities.</li>
  <li>🌐 <strong>Multi-lingual Support</strong>: Communicate effectively in multiple languages to assist diverse populations.</li>
  <li>🔋 <strong>Power-Efficient Design</strong>: Optimized for long battery life to remain operational during extended power outages.</li>
</ul>

<h2>🖼️ Screenshots</h2>

<div align="center">
  <img src="https://github.com/user-attachments/assets/1ed3b76c-66e1-42eb-9f30-ee64bce13358" alt="UI Screenshot" width="45%" style="margin-right: 10px;"/>

  <img src="https://github.com/user-attachments/assets/0c3988f3-a136-42b3-814b-117689352dd3" alt="Priority Mapping" width="45%"/>
  <img src="https://github.com/user-attachments/assets/7cd4525a-abd0-477e-9d83-2ea729635bb9" alt="Optimized Path" width="45%"/>


</div>

<h2>🛠️ Tech Stack</h2>

<ul>
  <li><strong>Frontend</strong>: Streamlit - for rapid development of interactive web applications</li>
  <li><strong>Backend</strong>: Python - leveraging its rich ecosystem of data science and AI libraries</li>
  <li><strong>Database</strong>: MongoDB Realtime Database - for real-time data synchronization and offline support</li>
  <li><strong>AI/ML</strong>: Google's Generative AI (Gemini) - powering intelligent conversations and decision-making</li>
  <li><strong>Geolocation</strong>: Custom WiFi & IP-based tracking - for accurate location services even in challenging environments</li>
  <li><strong>Text-to-Speech</strong>: ElevenLabs API - providing natural-sounding voice interactions</li>
  <li><strong>Mapping</strong>: KeplerGL - for advanced geospatial visualizations</li>
  <li><strong>Path Optimization</strong>: NVIDIA cuOpt - for efficient resource allocation and routing</li>
</ul>

<h2>🚀 Quick Start</h2>

<h3>

  



[Live Demo]([https://safeguardian-llm.streamlit.app/](https://github.com/Ashoka74/SafeGuardian-LLM.git))
  
</h3>

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/Ashoka74/SafeGuardian-LLM.git
cd SafeGuardian-LLM</code></pre>
  </li>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Set up environment variables:
    Create a <code>.env</code> file in the project root with the following content:
    <pre><code>
     gemini_api = '<YOUR_KEY>'
     elevenlabs_api = '<YOUR_KEY>'
</code></pre>
  </li>
  
 
  <li>Run the application:
    <pre><code>streamlit run app.py</code></pre>
  </li>
</ol>

<h2>🛠️ Usage Guide</h2>

<ol>
  <li><strong>Initial Setup</strong>:
    <ul>
      <li>Launch the app and grant necessary permissions (location, microphone, notifications).</li>
      <li>Create a user profile with essential information (medical conditions, emergency contacts).</li>
    </ul>
  </li>
  <li><strong>Emergency Activation</strong>:
    <ul>
      <li>Use the chat interface, voice command, or automatic detection to activate emergency mode.</li>
      <li>Provide details about your situation or immediate needs.</li>
    </ul>
  </li>
  <li><strong>AI Assistance</strong>:
    <ul>
      <li>Follow the AI assistant's guidance for emergency procedures and safety protocols.</li>
      <li>Receive personalized advice based on your profile and current situation.</li>
    </ul>
  </li>
  <li><strong>Resource Location</strong>:
    <ul>
      <li>Use the interactive map to locate nearby resources, safe zones, and emergency services.</li>
      <li>Get real-time updates on the availability and status of these resources.</li>
    </ul>
  </li>
  <li><strong>Community Coordination</strong>:
    <ul>
      <li>Connect with nearby users to coordinate local response efforts.</li>
      <li>Share and request resources within your community network.</li>
    </ul>
  </li>
  <li><strong>Offline Mode</strong>:
    <ul>
      <li>Access critical information and basic functionality even without an internet connection.</li>
      <li>Sync data automatically when connectivity is restored.</li>
    </ul>
  </li>
  <li><strong>Continuous Updates</strong>:
    <ul>
      <li>Stay informed with real-time updates on the evolving situation.</li>
      <li>Receive push notifications for critical alerts and changes in your area.</li>
    </ul>
  </li>
</ol>

<h2>🌍 Future Roadmap</h2>

<ol>
  <li><strong>Pilot Testing</strong> (Q3 2024):
    <ul>
      <li>Roll out SafeGuardianAI in high-risk areas to gather user feedback and refine features.</li>
      <li>Collaborate with local emergency response teams for real-world testing.</li>
    </ul>
  </li>
  <li><strong>Government Integration</strong> (Q4 2024):
    <ul>
      <li>Establish partnerships with public safety agencies to integrate SafeGuardianAI into existing emergency response frameworks.</li>
      <li>Develop secure data-sharing protocols to enhance coordination between users and official responders.</li>
    </ul>
  </li>
  <li><strong>Advanced AI Capabilities</strong> (Q1 2025):
    <ul>
      <li>Implement machine learning models for predictive analytics on disaster patterns and resource needs.</li>
      <li>Enhance natural language processing to improve multi-lingual support and context understanding.</li>
    </ul>
  </li>
  <li><strong>Global Language Expansion</strong> (Q2 2025):
    <ul>
      <li>Extend language support to cover 95% of global languages, including regional dialects.</li>
      <li>Implement real-time translation features for cross-language communication during international relief efforts.</li>
    </ul>
  </li>
  <li><strong>Wearable Integration</strong> (Q3 2025):
    <ul>
      <li>Develop APIs for smartwatch and fitness tracker integration to monitor vital signs and detect emergencies automatically.</li>
      <li>Create a dedicated SafeGuardianAI wearable device for enhanced tracking and communication in disaster zones.</li>
    </ul>
  </li>
  <li><strong>Community Resilience Features</strong> (Q4 2025):
    <ul>
      <li>Implement a community preparedness score and gamification elements to encourage proactive disaster readiness.</li>
      <li>Develop tools for community leaders to manage and coordinate larger groups during extended crisis periods.</li>
    </ul>
  </li>
  <li><strong>Scalability Enhancements</strong> (Ongoing):
    <ul>
      <li>Continuously optimize backend infrastructure to support millions of concurrent users.</li>
      <li>Implement edge computing solutions for faster response times and reduced server load.</li>
    </ul>
  </li>
</ol>


# Technical Diagram


```mermaid
sequenceDiagram
    participant U as User (Victim)
    participant D as Device (Smartphone)
    participant P as Permission Manager
    participant DS as Device Sensors
    participant LLM as On-Device LLM
    participant STT as Speech Engine
    participant M as Mesh Network
    participant S as Satellite Service
    participant C as Cloud (Firebase)
    participant CM as Cloud Model (Gemini/GPT)
    participant R as Rescue Teams
    participant N as Nearby Helpers

    Note over U,D: Earthquake Detected
    
    D->>D: Seismic activity detected
    D->>P: Request emergency permissions
    P->>U: "Grant emergency access?"
    Note over P,U: Location, Microphone,<br/>Sensors, Network, Storage
    U->>P: Grant all permissions
    
    P->>DS: Gather device capabilities
    DS-->>D: Location, Altitude, Battery
    DS-->>D: Accelerometer (AoA calc)
    DS-->>D: Network status, WiFi Direct, BLE
    DS-->>D: RAM, CPU, OS version
    DS-->>D: Available storage
    
    D->>D: Assess capabilities
    alt High-end device (RAM > 8GB, Fast CPU)
        D->>D: Load Qwen3-3B / Gemma-2B
        Note over D: >7 tokens/sec capable
        D->>STT: Initialize Whisper.cpp
    else Mid-range device
        D->>D: Load Phi-3.5 (3B)
        D->>STT: Use native Android/iOS STT
    else Low-end device
        D->>D: Queue for cloud processing
    end

    alt Cloud Available (Preferred for complex cases)
        U->>D: Voice input
        D->>CM: Stream to Gemini 2.0 Flash
        Note over CM: Native audio thinking<br/>Real-time processing
        CM->>D: Structured response + guidance
        D->>C: Store interaction
    else Local Processing Only
        U->>STT: Voice input
        STT->>LLM: Transcribed text
        LLM->>LLM: Process with llguidance
        Note over LLM: Structured generation<br/>JSON schema enforcement
        LLM->>U: Typed response + guidance
    end
    
    LLM->>D: Generate emergency packet
    Note over D: SOTA compression<br/>MessagePack/CBOR<br/>~90% size reduction
    
    D->>D: Priority queue by severity
    Note over D: Critical: <1KB packets<br/>Location + vitals only
    
    par Multi-path transmission attempts
        D->>M: BLE/WiFi mesh broadcast
        and
        D->>S: Satellite (if visible)
        and
        D->>C: Any available network
    end
    
    alt Mesh path succeeds
        M->>N: Relay packets
        N->>C: Forward to cloud
        C->>R: Push to rescue dashboard
        R->>C: Acknowledge receipt
        C->>M: Send pre-cached response
        M->>D: "Help acknowledged ETA: 45min"
        D->>U: Display confirmation
    else Direct cloud path
        C->>R: Real-time update
        R->>C: Mark handled + ETA
        C->>D: Cached response packet
        D->>U: "Rescue team notified"
    else All paths fail
        D->>D: Store with timestamp
        LLM->>U: "Data saved. Keep trying..."
        loop Retry every 30 seconds
            D->>D: Check connectivity
            D->>M: Attempt transmission
        end
    end
    
    loop Continuous monitoring
        DS->>D: Battery: {level}%
        DS->>D: Movement detected
        alt Battery < 20%
            D->>D: Switch to power save
            Note over D: Reduce model size<br/>Increase cache use
        end
        alt Status change detected
            U->>LLM: Update condition
            LLM->>D: Recompute priority
            D->>C: Send delta update only
        end
    end
    
    Note over R: Rescue approaching
    R->>C: "Team 500m away"
    C->>D: Priority push notification
    D->>U: "Rescue 5 min away"
    D->>D: Activate beacon mode
    Note over D: Max volume audio<br/>Flash light pattern<br/>Vibration sequence
```


```mermaid
graph TB
    subgraph "Layer 5: Emergency Services Integration"
        ES[Emergency Services Dashboard]
        CUOPT[NVIDIA CuOpt Route Optimization]
        TRIAGE[AI Triage System]
    end
    
    subgraph "Layer 4: Cloud Infrastructure"
        CLOUD[Firebase Cloud Services]
        API[API Gateway]
        SYNC[Data Synchronization]
        ANALYTICS[Analytics Engine]
    end
    
    subgraph "Layer 3: Gateway & Relay Systems"
        GATEWAY1[Mesh Gateway Nodes]
        GATEWAY2[Satellite Ground Stations]
        GATEWAY3[Cellular Edge Servers]
        RELAY[Community Relay Points]
    end
    
    subgraph "Layer 2: Network Transport"
        MESH[Bluetooth/WiFi Mesh Network]
        SAT[Satellite Communication]
        CELL[Cellular Network]
        LORA[LoRa Long Range]
    end
    
    subgraph "Layer 1: Device Layer"
        DEVICE1[Victim Device]
        DEVICE2[Helper Device]
        DEVICE3[Responder Device]
        LLM1[On-Device LLM]
        LLM2[On-Device LLM]
        LLM3[On-Device LLM]
    end
    
    %% Device connections
    DEVICE1 -.->|No Network| LLM1
    DEVICE2 -.->|No Network| LLM2
    DEVICE3 -.->|No Network| LLM3
    
    %% Layer 1 to Layer 2 connections
    DEVICE1 -->|BT/WiFi| MESH
    DEVICE1 -->|If Available| SAT
    DEVICE1 -->|If Available| CELL
    DEVICE1 -->|If Available| LORA
    
    DEVICE2 -->|BT/WiFi| MESH
    DEVICE2 -->|Primary| CELL
    
    DEVICE3 -->|All Channels| MESH
    DEVICE3 -->|All Channels| SAT
    DEVICE3 -->|All Channels| CELL
    DEVICE3 -->|All Channels| LORA
    
    %% Mesh network interconnections
    MESH <-->|Multi-hop| MESH
    
    %% Layer 2 to Layer 3 connections
    MESH --> GATEWAY1
    SAT --> GATEWAY2
    CELL --> GATEWAY3
    LORA --> RELAY
    
    GATEWAY1 <--> RELAY
    RELAY <--> GATEWAY3
    
    %% Layer 3 to Layer 4 connections
    GATEWAY1 --> API
    GATEWAY2 --> API
    GATEWAY3 --> API
    RELAY --> SYNC
    
    API --> CLOUD
    SYNC --> CLOUD
    CLOUD --> ANALYTICS
    
    %% Layer 4 to Layer 5 connections
    CLOUD --> ES
    ANALYTICS --> CUOPT
    ANALYTICS --> TRIAGE
    
    ES --> CUOPT
    CUOPT --> ES
    TRIAGE --> ES
    
    %% Styling
    classDef device fill:#e8f4f8,stroke:#2196F3,stroke-width:3px
    classDef network fill:#fff3e0,stroke:#ff9800,stroke-width:2px
    classDef gateway fill:#f3e5f5,stroke:#9c27b0,stroke-width:2px
    classDef cloud fill:#e8f5e9,stroke:#4caf50,stroke-width:2px
    classDef emergency fill:#ffebee,stroke:#f44336,stroke-width:3px
    
    class DEVICE1,DEVICE2,DEVICE3,LLM1,LLM2,LLM3 device
    class MESH,SAT,CELL,LORA network
    class GATEWAY1,GATEWAY2,GATEWAY3,RELAY gateway
    class CLOUD,API,SYNC,ANALYTICS cloud
    class ES,CUOPT,TRIAGE emergency
```


<h2>🤝 Contributing</h2>

<p>We welcome contributions to SafeGuardianAI! Whether you're fixing bugs, adding new features, or improving documentation, your help is appreciated. Please follow these steps to contribute:</p>

<ol>
  <li>Fork the repository</li>
  <li>Create your feature branch (<code>git checkout -b feature/AmazingFeature</code>)</li>
  <li>Commit your changes (<code>git commit -m 'Add some AmazingFeature'</code>)</li>
  <li>Push to the branch (<code>git push origin feature/AmazingFeature</code>)</li>
  <li>Open a Pull Request</li>
</ol>

<p>For major changes, please open an issue first to discuss what you would like to change. Please ensure to update tests as appropriate and adhere to the <a href="https://www.contributor-covenant.org/">Contributor Covenant</a> code of conduct.</p>

<h2>📄 License</h2>

<p>This project is licensed under the GNU General Public License- see the <a href="LICENSE.md">LICENSE.md</a> file for details.</p>

<h2>🙏 Acknowledgments</h2>

<ul>
  <li>Thanks to all the open-source projects that made SafeGuardianAI possible.</li>
  <li>Special thanks to our early adopters and beta testers for their valuable feedback.</li>
  <li>We're grateful to the emergency response professionals who provided insights into real-world disaster management challenges.</li>
</ul>

<hr>

<div align="center">
  <p>Made with ❤️ by the SafeGuardianAI Team</p>
</div>
