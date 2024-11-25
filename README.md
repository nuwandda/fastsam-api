
# FastSAM API

FastSAM API is a Python-based application designed to provide a high-performance service for computational tasks such as image segmentation and classification. Built using FastAPI, it offers a lightweight and robust framework for building scalable APIs.

With features like automatic documentation, modular architecture, and seamless Docker integration, this project is optimized for fast development, deployment, and use in production environments.

## Technical Details
FastSAM is a cutting-edge solution leveraging machine learning for fast and accurate image segmentation and classification tasks. It’s designed to handle high-throughput scenarios while maintaining accuracy.

The FastSAM engine uses:
* Efficient neural network architectures to process images with minimal latency.
* Optimized preprocessing pipelines for handling diverse image formats and resolutions.
* GPU acceleration for demanding workloads.

The system integrates with FastAPI to expose its capabilities via RESTful APIs, enabling easy integration into larger systems.

### Core Features
* Scalable API: Designed to handle multiple requests with low latency.
* Dockerized Deployment: Easily deployable across development, staging, and production environments.
* Automatic Documentation: Built-in Swagger UI for intuitive API interaction.
* Configurable Logging: Track and monitor application behavior and errors.

### Technologies Used
| Technologies | Purpose                                                                |
|--------------|------------------------------------------------------------------------|
| FastAPI      | High-performance Python web framework for building APIs.               |
| Uvicorn      | Lightning-fast ASGI server for running FastAPI applications.           |
| PyTorch      | Powering FastSAM’s machine learning models for image processing tasks. |
| Docker       | Containerization for consistent and portable deployments.              |
| Pytest       | For writing and executing test cases.                                  |
| Logging      | Python's logging module for application monitoring.                    |

## Important Notice
FastSAM API is optimized to run efficiently on CPUs.
Even without GPU acceleration, the application achieves excellent performance on most systems, making it a cost-effective choice for deployment in CPU-only environments.

### Running on a GPU
If you wish to run this module on a GPU for potentially faster processing on large-scale or complex workloads:
1. Ensure you have a compatible GPU and CUDA installed on your system.
2. Update the relevant sections in the implementation to use GPU-based PyTorch methods like below in **fastsam.py** file:

   ```bash
   service = FastSAMService(device='cuda')
   ```

Using a GPU may offer a speed boost in specific scenarios, but the FastSAM engine is specifically designed to perform exceptionally well on CPUs, keeping deployment costs low.

## Project Structure

```plaintext
fastsam_api/
├── app/
│   ├── __init__.py
│   ├── config.py            # Configuration settings
│   ├── main.py              # Main application file
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/       # API endpoint definitions
│   │   │   ├── __init__.py
│   │   │   ├── fastsam.py   # FastSAM-specific endpoints
│   │   ├── schemas/         # Request/response models
│   │   │   ├── __init__.py
│   │   │   ├── fastsam.py
│   ├── services/            # Business logic
│   │   ├── __init__.py
│   │   ├── fastsam_service.py
│   │   ├── fastsam/         # FastSAM files
│   │   ├── ultralytics/     # ultralytics files
│   │   ├── weights/         # Model weights
│   ├── utils/               # Helper functions/utilities
│   │   ├── __init__.py
│   │   ├── file_operations.py
│   │   ├── docker_utils.py
│   │   ├── logging.py       # Custom logging configuration
│   ├── models/              # (Optional) Database models if needed
│   │   ├── __init__.py
│   └── tests/               # Tests for all components
│       ├── __init__.py
│       ├── test_endpoints.py
│       ├── test_services.py
├── Dockerfile
├── requirements.txt
├── README.md
└── .env                    # Environment variables
```

## Requirements

- Python 3.9+
- Docker
- FastAPI
- Uvicorn
- Torch (Check requirements.txt for more)

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://gitlab.com/it740/refabric-selection.git
   cd fastsam_api
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory with necessary environment variables (e.g., `DATABASE_URL`, `DEBUG`, etc.).

4. **Run the application locally:**
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be accessible at `http://127.0.0.1:8000`.

## Dockerization

To run the application in a Docker container:

1. **Build the Docker image:**
   ```bash
   docker build -t fastsam_api .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -d -p 8000:8000 --env-file .env fastsam_api
   ```
   The API will be accessible at `http://localhost:8000`.

## Usage

FastSAM API documentation is automatically generated and available through Swagger UI. You can access it at:
```
http://localhost:8000/docs
```

### Example Endpoint

#### POST `/fastsam/`

Processes the provided data through FastSAM.

**Request:**
```json
{
  "data": "https://huggingface.co/spaces/An-619/FastSAM/resolve/main/examples/dogs.jpg"
}
```

**Response:**
```json
[
   [
      [
            0,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255
            .
            .
            .
```

## Testing

To run the tests:

```bash
pytest
```

The tests cover both endpoint functionality and business logic validation, ensuring the reliability of the FastSAM service.

## Logging

Logs are configured through `app/utils/logging.py`. Adjust the logging level and handlers as needed.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.
