import React, { useState } from 'react';
import { useAvailableSsids, updateWifiData } from '../../api/options';
import ErrorComponent from '../common/ErrorComponent';
import LoadingData from '../common/LoadingData';
import { confirmAndExecute } from '../../utils';
import { useTranslation } from 'react-i18next';

const WifiManager: React.FC = () => {
  const { data: ssids, isLoading, error } = useAvailableSsids();
  const [selectedSsid, setSelectedSsid] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const { t } = useTranslation();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    confirmAndExecute(t('wifi.connectToWifi', { selectedSsid }), () =>
      updateWifiData({ ssid: selectedSsid, password }),
    );
  };

  const dataValid = () => {
    return selectedSsid !== '' && password !== '';
  };

  if (isLoading) return <LoadingData />;
  if (error) return <ErrorComponent text={error.message} />;

  return (
    <div className='p-4 w-full max-w-3xl'>
      <h2 className='text-2xl text-center mb-4 text-secondary font-bold'>{t('wifi.setupWifi')}</h2>
      <form onSubmit={handleSubmit} className='grid grid-cols-1 md:grid-cols-2 gap-2'>
        <label className='text-neutral text-center'>
          SSID:
          <select
            value={selectedSsid}
            onChange={(e) => setSelectedSsid(e.target.value)}
            required
            className='select-base w-full !p-2'
          >
            <option value='' disabled>
              {t('wifi.selectSsid')}
            </option>
            {ssids?.map((ssid) => (
              <option key={ssid} value={ssid}>
                {ssid}
              </option>
            ))}
          </select>
        </label>
        <label className='text-neutral text-center'>
          {t('wifi.password')}:
          <input
            type='password'
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            className='input-base !p-2'
          />
        </label>
        <button
          type='submit'
          disabled={!dataValid()}
          className={`col-span-1 md:col-span-2 button-primary-filled p-2 mt-4 ${!dataValid() && 'disabled'}`}
        >
          {t('submit')}
        </button>
      </form>
    </div>
  );
};

export default WifiManager;
