import axios from 'axios';

export const fetchNegotiationInsights = async () => {
    try {
        const response = await axios.get('/api/insights');
        return response.data;
    } catch (error) {
        console.error('Error fetching negotiation insights:', error);
        throw error;
    }
}; 