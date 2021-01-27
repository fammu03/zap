package main

import (
	"github.com/adrg/xdg"
	"gopkg.in/yaml.v3"
	"os"
)

type ZapConfig struct {
	mirror 			string
	localStore 		string

}

func NewZapDefaultConfig() ZapConfig {
	localStore, err := xdg.DataFile("zap/v2")
	if err != nil {
		logger.Fatal("Could not find XDG path")
	}

	zapDefaultConfig := ZapConfig{
		mirror:     "https://g.srevinsaju.me/get-appimage/%s/core.json",
		localStore: localStore,
	}
	return zapDefaultConfig
}

func NewZapConfig(configPath string) (ZapConfig, error) {
	zapConfig := &ZapConfig{}

	if _, err := os.Stat(configPath); os.IsNotExist(err) {
		logger.Debug("No configuration found. Fall back to defaults")
		return *zapConfig, nil
	}

	file, err := os.Open(configPath)
	if err != nil {
		return ZapConfig{}, err
	}
	defer file.Close()

	// Init new YAML decode
	d := yaml.NewDecoder(file)

	// Start YAML decoding from file
	if err = d.Decode(&zapConfig); err != nil {
		return ZapConfig{}, err
	}

	return *zapConfig, nil
}

