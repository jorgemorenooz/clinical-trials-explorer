# 🧪 Clinical Trials Explorer (CTE)

A cloud-native platform for exploring, managing, and analyzing clinical trials data. It combines modern web technologies, healthcare interoperability standards (FHIR), and AI-driven analytics to simulate real-world clinical informatics solutions.

This project was developed as a personal initiative to apply computer science principles in the context of clinical trial regulation and health informatics. It serves as a technical demonstration aligned with trainee roles in research and innovation (e.g., at the European Medicines Agency).

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

### ✅ Phase 1: Design & Planning *(in progress)*
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
