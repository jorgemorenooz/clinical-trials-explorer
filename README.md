# 🧪 Clinical Trials Explorer (CTE)

A cloud-native platform for exploring, managing, and analyzing clinical trials data. It combines modern web technologies, healthcare interoperability standards (FHIR), and AI-driven analytics to simulate real-world clinical informatics solutions.

This project was developed as a personal initiative to apply computer science principles in the context of clinical trial regulation and health informatics. It serves as a technical demonstration aligned with trainee roles in research and innovation at the European Medicines Agency.

---

## 🎯 Project Goals

- Develop a full CRUD system for managing simulated clinical trials
- Integrate real data from public registries such as ClinicalTrials.gov
- Provide a RESTful API compatible with the FHIR standard
- Apply machine learning and generative AI for data summarization and insights
- Deploy the system using modern, cloud-based serverless architecture

---

## 🧰 Technologies Used

| Domain                  | Stack / Tools                                |
|-------------------------|----------------------------------------------|
| Backend                 | Python (FastAPI), PostgreSQL                 |
| Frontend                | React, TailwindCSS                           |
| External Data Source    | ClinicalTrials.gov API                       |
| Healthcare Standards    | HL7 FHIR (ResearchStudy resource)            |
| Cloud Infrastructure    | AWS Lambda, API Gateway, DynamoDB / RDS      |
| AI & ML                 | Transformers, Scikit-learn, pandas           |
| CI/CD & DevOps          | GitHub Actions, Terraform                    |

---

## 📁 Project Structure

clinical-trials-explorer/
├── k8s/postgres/ # Kubernetes YAML files for PostgreSQL Service
├── backend/ # FastAPI backend and RESTful logic
├── frontend/ # React application
├── fhir_module/ # FHIR data conversion adapters
├── ml_ai/ # AI/ML analysis and summarization scripts
├── cloud/ # AWS Lambda & infrastructure configuration
├── docs/ # Architecture diagrams and documentation
├── tests/ # Unit and integration tests
└── README.md


---

## 🚧 Project Phases

### ✅ Phase 1: Design & Planning
- [x] GitHub repository setup
- [x] Define tech stack and project scope
- [x] Draft initial architecture diagram
- [x] Prepare README with roadmap and objectives

### ⌛ Phase 2: Backend CRUD API
- [ ] Build a FastAPI app with PostgreSQL
- [ ] Define `ClinicalTrial` model (title, disease, status, location, date, description)
- [ ] Implement full REST endpoints
- [ ] Add unit tests with `pytest`

### ⌛ Phase 3: React Frontend
- [ ] Connect to API and display trials list
- [ ] Add forms for create/edit/delete
- [ ] Style the UI and validate input

### ⌛ Phase 4: External Data Integration
- [ ] Use ClinicalTrials.gov API to fetch real trials
- [ ] Merge with local data
- [ ] Enable filtering and search

### ⌛ Phase 5: AI & ML Analysis
- [ ] Summarize trial descriptions using LLMs
- [ ] Perform basic clustering or classification
- [ ] Generate visual insights (charts)

### ⌛ Phase 6: FHIR API Implementation
- [ ] Map local data to FHIR `ResearchStudy` structure
- [ ] Implement RESTful endpoint `/fhir/researchstudy/{id}`
- [ ] Validate FHIR format with example clients

### ⌛ Phase 7: Cloud Deployment
- [ ] Deploy backend on AWS Lambda + API Gateway
- [ ] Use DynamoDB or RDS in the cloud
- [ ] Host frontend on Vercel or S3 + CloudFront
- [ ] Add custom domain and HTTPS

### ⌛ Phase 8: Documentation & Demo
- [ ] Finalize `README.md` with screenshots
- [ ] Create Mermaid or Draw.io diagrams
- [ ] Record a short demo walkthrough (optional)

---

## 📌 Status

This project is under active development as part of a personal portfolio to demonstrate cloud, software engineering, AI, and health informatics skills in preparation for trainee opportunities in regulated healthcare environments.

---

## 📄 License

MIT License — feel free to use and adapt for educational purposes.

## 1️⃣ Phase 1: Design & Planning

### ✅ Step 1: MVP Scope for Clinical Trials Explorer
- Users can create, read, update, and delete simulated clinical trial entries via a REST API.
- The backend provides a RESTful interface, exposing clinical trial data in a structured JSON format.
- The system can fetch and display real clinical trials from ClinicalTrials.gov using their public API.
- The frontend web app (React) allows users to view and filter clinical trials from both local and external sources.
- The backend includes an endpoint that returns clinical trials in FHIR-compatible format (e.g., ResearchStudy resource).
- All components (frontend, backend, data access) are modular, and the system can be deployed locally or to the cloud.

While real-time data is fetched from ClinicalTrials.gov for technical demonstration purposes, this application is conceptually aligned with EMA’s CTIS platform and the EU Clinical Trials Regulation.

---

### ✅ Step 2: Designing the `ClinicalTrial` Data Model

The main data entity in this application is a `ClinicalTrial`, structured to reflect core fields aligned with clinical research standards and compatible with future FHIR transformation.

#### 📄 Fields

- `id` — unique identifier (UUID or numeric)
- `official_title` — full official title of the trial
- `acronym` — short name or abbreviation
- `disease_area` — condition being studied (e.g., Diabetes)
- `trial_phase` — clinical phase (e.g., Phase I, II, III)
- `status` — current status (Ongoing, Completed, etc.)
- `start_date` — trial start date
- `end_date` — trial end date
- `country` — where the trial is conducted
- `sponsor` — sponsoring organization or entity
- `description` — full protocol or study summary

---

### ✅ Step 3: Choosing and Deploying the Database
PostgreSQL was selected over NoSQL solutions due to:

- Structured schema enforcement
- Strong support for complex queries (filtering by status, phase, etc.)
- Easy integration with healthcare data standards like **FHIR**
- Compatibility with both local development and future **cloud migration (Azure/AWS)**

To avoid installing a local PostgreSQL client, the database is deployed **inside a Kubernetes cluster** using **Minikube** and containerized via the official `postgres:15` image.

---

#### 🧰 Tools Used

- [Minikube](https://minikube.sigs.k8s.io/docs/start/) — local Kubernetes cluster
- [Docker](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-win-amd64) — used as the container runtime for Minikube
- kubectl — Kubernetes CLI
- PostgreSQL 15 — running as a pod inside Kubernetes
- Kubernetes YAML manifests — to define `Secret`, `PVC`, `Deployment`, and `Service` in `k8s/postgres`

---

#### 🔧 Install Minikube on Windows
Start Minikube with Docker driver:

   ```powershell
   minikube start --driver=docker
   ```

Verify the cluster is running:

   ```powershell
   kubectl get nodes
   ```

---

#### 🚀 Deploy PostgreSQL to Minikube
Apply the Kubernetes manifests (defined in `k8s/postgres`) to deploy the PostgreSQL database and its supporting resources:

   ```powershell
   kubectl apply -f k8s/postgres/
   ```

This will create:

- A Kubernetes Secret with the database credentials
- A PersistentVolumeClaim for PostgreSQL data
- A Deployment running the postgres:15 container
- A Service to expose PostgreSQL within the cluster

In order to verify that PostgreSQL is accessible by launching a temporary pod and connecting to the service:

   ```powershell
   kubectl run test-client --rm -it --image=postgres:15 -- bash
   ```
Then inside the container::

   ```powershell
   psql -h postgres -U postgres -d clinical_trials
   # password: postgres
   ```

---

#### 📄 View Logs (Optional)

To confirm it started properly and the env vars (from the secret) are working:

   ```powershell
   kubectl logs deployment/postgres
   ```

We are looking for log lines like: `PostgreSQL init process complete; ready for start up.`