import React, { useState, useEffect } from 'react';
import styled, { ThemeProvider, createGlobalStyle } from 'styled-components';
import { useForm } from 'react-hook-form';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';

// Theme definitions
const lightTheme = {
  colors: {
    primary: '#2563eb',
    primaryHover: '#1d4ed8',
    secondary: '#64748b',
    success: '#059669',
    error: '#dc2626',
    warning: '#d97706',
    background: '#ffffff',
    surface: '#f8fafc',
    surfaceHover: '#f1f5f9',
    text: '#1e293b',
    textSecondary: '#64748b',
    textMuted: '#94a3b8',
    border: '#e2e8f0',
    borderHover: '#cbd5e1',
    shadow: 'rgba(0, 0, 0, 0.1)',
    shadowHover: 'rgba(0, 0, 0, 0.15)',
  },
  gradients: {
    primary: 'linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%)',
    surface: 'linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%)',
  }
};

const darkTheme = {
  colors: {
    primary: '#3b82f6',
    primaryHover: '#2563eb',
    secondary: '#94a3b8',
    success: '#10b981',
    error: '#ef4444',
    warning: '#f59e0b',
    background: '#0f172a',
    surface: '#1e293b',
    surfaceHover: '#334155',
    text: '#f1f5f9',
    textSecondary: '#cbd5e1',
    textMuted: '#94a3b8',
    border: '#334155',
    borderHover: '#475569',
    shadow: 'rgba(0, 0, 0, 0.3)',
    shadowHover: 'rgba(0, 0, 0, 0.4)',
  },
  gradients: {
    primary: 'linear-gradient(135deg, #3b82f6 0%, #2563eb 100%)',
    surface: 'linear-gradient(135deg, #1e293b 0%, #334155 100%)',
  }
};

// Global styles
const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
    background: ${props => props.theme.colors.background};
    color: ${props => props.theme.colors.text};
    transition: background-color 0.3s ease, color 0.3s ease;
  }
`;

const FormContainer = styled.div`
  background: ${props => props.theme.colors.background};
  border-radius: 16px;
  padding: 40px;
  box-shadow: 0 20px 40px ${props => props.theme.colors.shadow};
  margin-bottom: 30px;
  border: 1px solid ${props => props.theme.colors.border};
  transition: all 0.3s ease;
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  gap: 30px;
`;

const Section = styled.div`
  border: 1px solid ${props => props.theme.colors.border};
  border-radius: 12px;
  padding: 24px;
  background: ${props => props.theme.colors.surface};
  transition: all 0.3s ease;
  
  &:hover {
    border-color: ${props => props.theme.colors.borderHover};
  }
`;

const SectionTitle = styled.h3`
  color: ${props => props.theme.colors.text};
  font-size: 1.25rem;
  margin-bottom: 20px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
`;

const DropzoneContainer = styled.div`
  border: 2px dashed ${props => props.isDragActive ? props.theme.colors.primary : props.theme.colors.border};
  border-radius: 12px;
  padding: 40px;
  text-align: center;
  background: ${props => props.isDragActive ? props.theme.colors.surfaceHover : props.theme.colors.background};
  cursor: pointer;
  transition: all 0.3s ease;
  
  &:hover {
    border-color: ${props => props.theme.colors.primary};
    background: ${props => props.theme.colors.surfaceHover};
  }
`;

const DropzoneText = styled.p`
  color: ${props => props.theme.colors.textSecondary};
  font-size: 1.1rem;
  margin: 10px 0;
  font-weight: 500;
`;

const FileInfo = styled.div`
  background: ${props => props.theme.colors.success}15;
  border: 1px solid ${props => props.theme.colors.success};
  border-radius: 8px;
  padding: 15px;
  margin-top: 15px;
  color: ${props => props.theme.colors.success};
  font-weight: 500;
`;

const InputGroup = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 20px;
`;

const InputContainer = styled.div`
  display: flex;
  flex-direction: column;
`;

const Label = styled.label`
  color: ${props => props.theme.colors.text};
  font-weight: 500;
  margin-bottom: 8px;
  font-size: 0.95rem;
`;

const Input = styled.input`
  padding: 12px 16px;
  border: 2px solid ${props => props.theme.colors.border};
  border-radius: 8px;
  font-size: 1rem;
  background: ${props => props.theme.colors.background};
  color: ${props => props.theme.colors.text};
  transition: all 0.3s ease;
  
  &:focus {
    outline: none;
    border-color: ${props => props.theme.colors.primary};
    box-shadow: 0 0 0 3px ${props => props.theme.colors.primary}20;
  }
  
  &::placeholder {
    color: ${props => props.theme.colors.textMuted};
  }
`;

const Select = styled.select`
  padding: 12px 16px;
  border: 2px solid ${props => props.theme.colors.border};
  border-radius: 8px;
  font-size: 1rem;
  background: ${props => props.theme.colors.background};
  color: ${props => props.theme.colors.text};
  transition: all 0.3s ease;
  
  &:focus {
    outline: none;
    border-color: ${props => props.theme.colors.primary};
    box-shadow: 0 0 0 3px ${props => props.theme.colors.primary}20;
  }
`;

const CheckboxContainer = styled.div`
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 20px 0;
`;

const Checkbox = styled.input`
  width: 20px;
  height: 20px;
  accent-color: ${props => props.theme.colors.primary};
`;

const Button = styled.button`
  background: ${props => props.theme.gradients.primary};
  color: white;
  border: none;
  padding: 16px 32px;
  border-radius: 12px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin: 10px;
  box-shadow: 0 4px 12px ${props => props.theme.colors.primary}30;
  
  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px ${props => props.theme.colors.primary}40;
  }
  
  &:disabled {
    opacity: 0.6;
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
  }
`;

const LoadingSpinner = styled.div`
  display: inline-block;
  width: 20px;
  height: 20px;
  border: 3px solid #ffffff;
  border-radius: 50%;
  border-top-color: transparent;
  animation: spin 1s ease-in-out infinite;
  margin-right: 10px;
  
  @keyframes spin {
    to { transform: rotate(360deg); }
  }
`;

const ErrorMessage = styled.div`
  background: ${props => props.theme.colors.error}15;
  border: 1px solid ${props => props.theme.colors.error};
  color: ${props => props.theme.colors.error};
  padding: 16px;
  border-radius: 8px;
  margin: 20px 0;
  font-weight: 500;
`;

const SuccessMessage = styled.div`
  background: ${props => props.theme.colors.success}15;
  border: 1px solid ${props => props.theme.colors.success};
  color: ${props => props.theme.colors.success};
  padding: 16px;
  border-radius: 8px;
  margin: 20px 0;
  font-weight: 500;
`;

const PlayerSection = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 30px;
  
  @media (max-width: 768px) {
    grid-template-columns: 1fr;
  }
`;

const PlayerGroup = styled.div`
  background: ${props => props.theme.colors.background};
  padding: 24px;
  border-radius: 12px;
  border: 1px solid ${props => props.theme.colors.border};
  transition: all 0.3s ease;
  
  &:hover {
    border-color: ${props => props.theme.colors.borderHover};
  }
`;

const PlayerTitle = styled.h4`
  color: ${props => props.theme.colors.text};
  margin-bottom: 20px;
  text-align: center;
  font-size: 1.2rem;
  font-weight: 600;
`;

const PlayerInputs = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
`;

const PlayerInput = styled.input`
  padding: 12px 16px;
  border: 2px solid ${props => props.theme.colors.border};
  border-radius: 8px;
  font-size: 0.95rem;
  background: ${props => props.theme.colors.background};
  color: ${props => props.theme.colors.text};
  transition: all 0.3s ease;
  
  &:focus {
    outline: none;
    border-color: ${props => props.theme.colors.primary};
    box-shadow: 0 0 0 3px ${props => props.theme.colors.primary}20;
  }
  
  &::placeholder {
    color: ${props => props.theme.colors.textMuted};
  }
`;

// Theme toggle component
const ThemeToggle = styled.button`
  position: fixed;
  top: 20px;
  right: 20px;
  background: ${props => props.theme.colors.surface};
  border: 2px solid ${props => props.theme.colors.border};
  border-radius: 50px;
  padding: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  z-index: 1000;
  box-shadow: 0 4px 12px ${props => props.theme.colors.shadow};
  
  &:hover {
    border-color: ${props => props.theme.colors.primary};
    transform: scale(1.05);
  }
`;

const AppContainer = styled.div`
  min-height: 100vh;
  background: ${props => props.theme.colors.background};
  padding: 20px;
  transition: background-color 0.3s ease;
`;

const Header = styled.div`
  text-align: center;
  margin-bottom: 40px;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
`;

const Title = styled.h1`
  color: ${props => props.theme.colors.text};
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 10px;
  background: ${props => props.theme.gradients.primary};
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
`;

const Subtitle = styled.p`
  color: ${props => props.theme.colors.textSecondary};
  font-size: 1.2rem;
  font-weight: 400;
`;

const MainContent = styled.div`
  max-width: 1200px;
  margin: 0 auto;
`;

function SportsAnalysisForm() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [message, setMessage] = useState({ type: '', text: '' });
  const [arenaToggled, setArenaToggled] = useState(false);
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [downloadUrl, setDownloadUrl] = useState(null);
  const [downloadFileName, setDownloadFileName] = useState(null);
  
  // Load theme preference from localStorage
  useEffect(() => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      setIsDarkMode(savedTheme === 'dark');
    }
  }, []);
  
  // Save theme preference to localStorage
  useEffect(() => {
    localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
  }, [isDarkMode]);
  
  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
  };
  
  const { register, handleSubmit } = useForm({
    defaultValues: {
      option: 'other',
      handicap_goals_winning: 0,
      handicap_goals_losing: 0,
      team1_player1: 'team 1 player 1',
      team1_player2: 'team 1 player 2',
      team1_player3: 'team 1 player 3',
      team1_player4: 'team 1 player 4',
      team1_goal1: -99,
      team1_goal2: -99,
      team1_goal3: -99,
      team1_goal4: -99,
      team2_player1: 'team 2 player 1',
      team2_player2: 'team 2 player 2',
      team2_player3: 'team 2 player 3',
      team2_player4: 'team 2 player 4',
      team2_goal1: -99,
      team2_goal2: -99,
      team2_goal3: -99,
      team2_goal4: -99
    }
  });

  const onDrop = (acceptedFiles) => {
    const file = acceptedFiles[0];
    if (file && file.type === 'text/csv') {
      setSelectedFile(file);
      setMessage({ type: 'success', text: `File selected: ${file.name}` });
    } else {
      setMessage({ type: 'error', text: 'Please select a valid CSV file' });
    }
  };

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'text/csv': ['.csv']
    },
    multiple: false
  });

  const onSubmit = async (data) => {
    if (!selectedFile) {
      setMessage({ type: 'error', text: 'Please select a CSV file' });
      return;
    }

    setIsLoading(true);
    setMessage({ type: '', text: '' });
    setDownloadUrl(null);
    setDownloadFileName(null);

    const formData = new FormData();
    formData.append('file', selectedFile);
    
    // Add all form data
    Object.keys(data).forEach(key => {
      formData.append(key, data[key]);
    });
    formData.append('arena_toggled', arenaToggled);

    try {
      const response = await axios.post('/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (response.data.success) {
        setMessage({ type: 'success', text: 'Analysis completed successfully! Downloading Word document...' });
        
        // Download the generated file
        if (response.data.file_url) {
          const fullUrl = `/api${response.data.file_url}`;
          setDownloadUrl(fullUrl);
          
          // Generate filename based on CSV file name
          const csvFileName = selectedFile.name;
          const baseName = csvFileName.replace(/\.csv$/i, '');
          const wordFileName = `${baseName}_analysis.docx`;
          
          // Store filename for manual download
          setDownloadFileName(wordFileName);
          
          try {
            const link = document.createElement('a');
            link.href = fullUrl;
            link.download = wordFileName;
            link.target = '_blank';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            
            // Update success message after download attempt
            setTimeout(() => {
              setMessage({ type: 'success', text: 'Analysis completed successfully! Word document downloaded.' });
            }, 1000);
          } catch (downloadError) {
            console.error('Download error:', downloadError);
            setMessage({ type: 'error', text: 'Analysis completed but file download failed. Please try downloading manually.' });
          }
        } else {
          setMessage({ type: 'error', text: 'Analysis completed but no file URL provided.' });
        }
      } else {
        setMessage({ type: 'error', text: response.data.message || 'Analysis failed' });
      }
    } catch (error) {
      console.error('Analysis error:', error);
      let errorMessage = 'An error occurred during analysis';
      
      if (error.response) {
        // Server responded with error status
        errorMessage = error.response.data?.detail || error.response.data?.message || `Server error: ${error.response.status}`;
      } else if (error.request) {
        // Request was made but no response received
        errorMessage = 'Network error: Unable to connect to the server. Please check your connection.';
      } else {
        // Something else happened
        errorMessage = error.message || 'An unexpected error occurred';
      }
      
      setMessage({ 
        type: 'error', 
        text: errorMessage
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <ThemeProvider theme={isDarkMode ? darkTheme : lightTheme}>
      <GlobalStyle />
      <AppContainer>
        <ThemeToggle onClick={toggleTheme}>
          {isDarkMode ? '☀️' : '🌙'}
        </ThemeToggle>
        
        <Header>
          <Title>Sports Analysis</Title>
          <Subtitle>Upload your sports data and generate comprehensive reports</Subtitle>
        </Header>
        
        <MainContent>
          <FormContainer>
          <Form onSubmit={handleSubmit(onSubmit)}>
            {/* File Upload Section */}
            <Section>
              <SectionTitle>📁 Upload CSV File</SectionTitle>
          <DropzoneContainer {...getRootProps()} isDragActive={isDragActive}>
            <input {...getInputProps()} />
            <DropzoneText>
              {isDragActive
                ? 'Drop the CSV file here...'
                : 'Drag & drop a CSV file here, or click to select'}
            </DropzoneText>
          </DropzoneContainer>
          {selectedFile && (
            <FileInfo>
              ✓ Selected: {selectedFile.name} ({(selectedFile.size / 1024).toFixed(1)} KB)
            </FileInfo>
          )}
        </Section>

        {/* Analysis Options */}
        <Section>
          <SectionTitle>⚙️ Analysis Options</SectionTitle>
          <InputGroup>
            <InputContainer>
              <Label>Match Type</Label>
              <Select {...register('option')}>
                <option value="other">Other</option>
                <option value="Subsidiary final">Subsidiary Final</option>
                <option value="Semifinal">Semi Final</option>
                <option value="Final">Final</option>
              </Select>
            </InputContainer>
            <InputContainer>
              <Label>Handicap Goals (Winning Team)</Label>
              <Input
                type="number"
                step="0.1"
                {...register('handicap_goals_winning', { valueAsNumber: true })}
              />
            </InputContainer>
            <InputContainer>
              <Label>Handicap Goals (Losing Team)</Label>
              <Input
                type="number"
                step="0.1"
                {...register('handicap_goals_losing', { valueAsNumber: true })}
              />
            </InputContainer>
          </InputGroup>
          
          <CheckboxContainer>
            <Checkbox
              type="checkbox"
              id="arena"
              checked={arenaToggled}
              onChange={(e) => setArenaToggled(e.target.checked)}
            />
            <Label htmlFor="arena">Arena Mode (3 players only)</Label>
          </CheckboxContainer>
        </Section>

        {/* Player Information */}
        <Section>
          <SectionTitle>👥 Player Information</SectionTitle>
          <PlayerSection>
            <PlayerGroup>
              <PlayerTitle>Team 1 Players</PlayerTitle>
              <PlayerInputs>
                <PlayerInput
                  placeholder="Player 1 Name"
                  {...register('team1_player1')}
                />
                <PlayerInput
                  type="number"
                  step="0.1"
                  placeholder="Order"
                  {...register('team1_goal1', { valueAsNumber: true })}
                />
                <PlayerInput
                  placeholder="Player 2 Name"
                  {...register('team1_player2')}
                />
                <PlayerInput
                  type="number"
                  step="0.1"
                  placeholder="Order"
                  {...register('team1_goal2', { valueAsNumber: true })}
                />
                <PlayerInput
                  placeholder="Player 3 Name"
                  {...register('team1_player3')}
                />
                <PlayerInput
                  type="number"
                  step="0.1"
                  placeholder="Order"
                  {...register('team1_goal3', { valueAsNumber: true })}
                />
                {!arenaToggled && (
                  <>
                    <PlayerInput
                      placeholder="Player 4 Name"
                      {...register('team1_player4')}
                    />
                    <PlayerInput
                      type="number"
                      step="0.1"
                      placeholder="Order"
                      {...register('team1_goal4', { valueAsNumber: true })}
                    />
                  </>
                )}
              </PlayerInputs>
            </PlayerGroup>

            <PlayerGroup>
              <PlayerTitle>Team 2 Players</PlayerTitle>
              <PlayerInputs>
                <PlayerInput
                  placeholder="Player 1 Name"
                  {...register('team2_player1')}
                />
                <PlayerInput
                  type="number"
                  step="0.1"
                  placeholder="Order"
                  {...register('team2_goal1', { valueAsNumber: true })}
                />
                <PlayerInput
                  placeholder="Player 2 Name"
                  {...register('team2_player2')}
                />
                <PlayerInput
                  type="number"
                  step="0.1"
                  placeholder="Order"
                  {...register('team2_goal2', { valueAsNumber: true })}
                />
                <PlayerInput
                  placeholder="Player 3 Name"
                  {...register('team2_player3')}
                />
                <PlayerInput
                  type="number"
                  step="0.1"
                  placeholder="Order"
                  {...register('team2_goal3', { valueAsNumber: true })}
                />
                {!arenaToggled && (
                  <>
                    <PlayerInput
                      placeholder="Player 4 Name"
                      {...register('team2_player4')}
                    />
                    <PlayerInput
                      type="number"
                      step="0.1"
                      placeholder="Order"
                      {...register('team2_goal4', { valueAsNumber: true })}
                    />
                  </>
                )}
              </PlayerInputs>
            </PlayerGroup>
          </PlayerSection>
        </Section>


        {/* Messages */}
        {message.text && (
          message.type === 'error' ? (
            <ErrorMessage>{message.text}</ErrorMessage>
          ) : (
            <SuccessMessage>{message.text}</SuccessMessage>
          )
        )}

        {/* Manual Download Button */}
        {downloadUrl && (
          <Section>
            <SectionTitle>📥 Download Report</SectionTitle>
            <Button 
              type="button" 
              onClick={() => {
                const link = document.createElement('a');
                link.href = downloadUrl;
                link.download = downloadFileName || 'sports_analysis.docx';
                link.target = '_blank';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
              }}
            >
              Download {downloadFileName || 'Word Document'}
            </Button>
          </Section>
        )}

        {/* Submit Button */}
        <Button type="submit" disabled={isLoading}>
          {isLoading && <LoadingSpinner />}
          {isLoading ? 'Processing...' : 'Generate Analysis Report'}
            </Button>
          </Form>
        </FormContainer>
        </MainContent>
      </AppContainer>
    </ThemeProvider>
  );
}

export default SportsAnalysisForm;
