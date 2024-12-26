import React, { createContext, useState, useEffect, useContext } from 'react';
import { getConfigValues } from './api/options';
import { DefinedConfigData } from './types/models';
import { useTranslation } from 'react-i18next';

interface IConfig {
  config: DefinedConfigData;
  refetchConfig: () => Promise<void>;
  theme: string;
  changeTheme: (theme: string) => void;
}

const STORE_THEME: string = 'THEME';
const STORE_CONFIG: string = 'CONFIG';
const ConfigContext = createContext({} as IConfig);

export const ConfigProvider = ({ children }: { children: React.ReactNode }) => {
  const [config, setConfig] = useState<DefinedConfigData>(JSON.parse(localStorage.getItem(STORE_CONFIG) || '{}'));
  const [theme, setTheme] = useState<string>(localStorage.getItem(STORE_THEME) || '');
  const { i18n } = useTranslation();

  const fetchConfigValues = async () => {
    const configValues = await getConfigValues();
    const makerTheme = configValues.MAKER_THEME;
    if (makerTheme !== undefined) {
      setTheme(makerTheme.toString());
    }
    setConfig(configValues);
  };

  useEffect(() => {
    fetchConfigValues();
  }, []);

  useEffect(() => {
    if (theme) {
      document.documentElement.className = theme;
      document.body.className = theme;
      localStorage.setItem(STORE_THEME, theme);
    }
  }, [theme]);

  useEffect(() => {
    localStorage.setItem(STORE_CONFIG, JSON.stringify(config));
    i18n.changeLanguage(config?.UI_LANGUAGE || 'en');
  }, [config]);

  const handleThemeChange = (newTheme: string) => {
    setTheme(newTheme);
  };

  return (
    <ConfigContext.Provider
      value={{
        config,
        refetchConfig: fetchConfigValues,
        theme,
        changeTheme: handleThemeChange,
      }}
    >
      {children}
    </ConfigContext.Provider>
  );
};

export const useConfig = () => useContext(ConfigContext);
