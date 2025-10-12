# Sports Analysis Application

A modern React + FastAPI application for sports data analysis and report generation, fully containerized with Docker Compose.

## Features

- **Modern UI**: Beautiful React frontend with drag-and-drop file upload
- **FastAPI Backend**: High-performance Python API with automatic documentation
- **Docker Support**: Full containerization for easy deployment
- **Modular Architecture**: Clean, maintainable code structure
- **Real-time Processing**: Upload CSV files and generate Word reports instantly

## Project Structure

```
├── backend/                 # FastAPI backend (Docker)
│   ├── api/                # API routes and models
│   ├── services/           # Business logic
│   ├── utils/              # Utility functions
│   ├── static/             # Generated files
│   ├── main.py             # FastAPI app entry point
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Backend container config
├── frontend/               # React frontend (Docker)
│   ├── src/                # React source code
│   ├── public/             # Static assets
│   ├── package.json        # Node dependencies
│   ├── Dockerfile          # Frontend container config
│   └── nginx.conf          # Nginx configuration
├── docker-compose.yml      # Full orchestration
└── README.md              # This file
```

## Quick Start

### Prerequisites

- Docker and Docker Compose installed
- Git (for cloning the repository)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd sports-analysis-app
   ```

2. **Start the application**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Usage

1. **Upload CSV File**: Drag and drop or click to select a CSV file containing sports data
2. **Configure Analysis**: Select match type, handicap goals, and player information
3. **Generate Report**: Click "Generate Analysis Report" to process the data
4. **Download Results**: The generated Word document will be automatically downloaded

## API Endpoints

- `POST /upload` - Upload and analyze CSV file
- `GET /download/{filename}` - Download generated files
- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation

## Development

### Backend Development

The backend uses FastAPI with the following key features:
- Automatic API documentation
- Request/response validation with Pydantic
- CORS support for frontend integration
- Modular service architecture

### Frontend Development

The frontend is built with React and includes:
- Modern UI with styled-components
- Drag-and-drop file upload
- Form validation with react-hook-form
- Responsive design

### Adding New Features

1. **Backend**: Add new routes in `backend/api/routes.py` and services in `backend/services/`
2. **Frontend**: Add new components in `frontend/src/components/`
3. **Docker**: Update Dockerfile if new dependencies are added

## Troubleshooting

### Common Issues

1. **Port conflicts**: Ensure ports 3000 and 8000 are available
2. **File permissions**: Check Docker volume permissions
3. **Build failures**: Clear Docker cache with `docker-compose build --no-cache`
4. **CORS issues**: Make sure backend is running on port 8000

### Logs

View backend logs:
```bash
docker-compose logs backend
```

### Cleanup

Stop and remove backend container:
```bash
docker-compose down
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Docker Compose
5. Submit a pull request

## License

This project is licensed under the MIT License.