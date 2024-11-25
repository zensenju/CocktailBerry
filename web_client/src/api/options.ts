import { useQuery, UseQueryResult } from 'react-query';
import axios from 'axios';
import { API_URL } from './common';

const options_url = `${API_URL}/options`;

export const getOptions = async (): Promise<any[]> => {
  return axios
    .get<any[]>(options_url)
    .then((res) => res.data)
    .catch((error) => {
      console.error('Error fetching options:', error);
      return [];
    });
};

export const useOptions = (): UseQueryResult<any[], Error> => {
  return useQuery<any[], Error>('options', getOptions);
};

export const updateOptions = async (options: Record<string, any>): Promise<{ message: string }> => {
  return axios
    .post<{ message: string }>(options_url, options, {
      headers: {
        'Content-Type': 'application/json',
      },
    })
    .then((res) => res.data);
};

export const cleanMachine = async (): Promise<{ message: string }> => {
  return axios.post<{ message: string }>(`${options_url}/clean`).then((res) => res.data);
};

export const rebootSystem = async (): Promise<{ message: string }> => {
  return axios.post<{ message: string }>(`${options_url}/reboot`).then((res) => res.data);
};

export const shutdownSystem = async (): Promise<{ message: string }> => {
  return axios.post<{ message: string }>(`${options_url}/shutdown`).then((res) => res.data);
};

export const createBackup = async (location: string): Promise<{ message: string }> => {
  return axios
    .get<{ message: string }>(`${options_url}/backup`, {
      params: { location },
    })
    .then((res) => res.data);
};

export const uploadBackup = async (location: string): Promise<{ message: string }> => {
  return axios
    .post<{ message: string }>(
      `${options_url}/backup`,
      { location },
      {
        headers: {
          'Content-Type': 'application/json',
        },
      },
    )
    .then((res) => res.data);
};

export const getLogs = async (): Promise<{ message: string }> => {
  return axios.get<{ message: string }>(`${options_url}/logs`).then((res) => res.data);
};

export const useLogs = (): UseQueryResult<{ message: string }, Error> => {
  return useQuery<{ message: string }, Error>('logs', getLogs);
};

export const getRfidWriter = async (): Promise<{ message: string }> => {
  return axios.get<{ message: string }>(`${options_url}/rfid`).then((res) => res.data);
};

export const updateWifiData = async (): Promise<{ message: string }> => {
  return axios.post<{ message: string }>(`${options_url}/wifi`).then((res) => res.data);
};

export const getAddonData = async (): Promise<{ message: string }> => {
  return axios.get<{ message: string }>(`${options_url}/addon`).then((res) => res.data);
};

export const checkInternetConnection = async (): Promise<{ is_connected: boolean }> => {
  return axios.get<{ is_connected: boolean }>(`${options_url}/connection`).then((res) => res.data);
};

export const updateSystem = async (): Promise<{ message: string }> => {
  return axios.post<{ message: string }>(`${options_url}/update/system`).then((res) => res.data);
};

export const updateSoftware = async (): Promise<{ message: string }> => {
  return axios.post<{ message: string }>(`${options_url}/update/software`).then((res) => res.data);
};
