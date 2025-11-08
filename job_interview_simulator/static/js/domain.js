let jobDescriptions = {};  // Empty object to store the fetched job descriptions
let currentJob = '';

// Function to load job descriptions from the JSON file
function loadJobDescriptions() {
    fetch('jobDescriptions.json')  // Adjust the path if necessary
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to load job descriptions');
            }
            return response.json();
        })
        .then(data => {
            jobDescriptions = data;  // Assign the loaded data to the global variable
            console.log('Job descriptions loaded:', jobDescriptions);
            addButtonListeners();  // Enable the buttons after loading the data
        })
        .catch(error => {
            console.error('Error loading job descriptions:', error);
        });
}

// Function to attach event listeners to job buttons after data is loaded
function addButtonListeners() {
    const jobButtons = document.querySelectorAll('.job-btn');
    jobButtons.forEach(button => {
        button.addEventListener('click', () => {
            const jobType = button.getAttribute('data-job-type');  // Assuming buttons have a data-job-type attribute
            showJobDescription(jobType);  // Show job description based on the button clicked
        });
    });
}

// Function to display the job description based on the selected job type
function showJobDescription(jobType) {
    if (!jobDescriptions[jobType]) {
        console.error('Job type not found:', jobType);
        return;
    }

    const job = jobDescriptions[jobType];
    currentJob = jobType;

    // Update the job title and summary
    document.getElementById('job-title').innerText = job.title;
    document.getElementById('job-summary').innerText = job.summary || '';

    // Update responsibilities
    const responsibilitiesList = document.getElementById('job-responsibilities');
    responsibilitiesList.innerHTML = '';
    if (job.responsibilities && job.responsibilities.length > 0) {
        job.responsibilities.forEach(res => {
            const li = document.createElement('li');
            li.innerText = res;
            responsibilitiesList.appendChild(li);
        });
    } else {
        responsibilitiesList.innerHTML = '<li>No specific responsibilities listed.</li>';
    }

    // Update requirements
    const requirementsList = document.getElementById('requirements');
    requirementsList.innerHTML = '';
    if (job.requirements && job.requirements.length > 0) {
        job.requirements.forEach(req => {
            const li = document.createElement('li');
            li.innerText = req;
            requirementsList.appendChild(li);
        });
    } else {
        requirementsList.innerHTML = '<li>No specific requirements listed.</li>';
    }
}

// Load job descriptions when the page loads
document.addEventListener('DOMContentLoaded', loadJobDescriptions);
