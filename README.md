## Installation ##
```shell
brew install selenium-server-standalone  
ln -sfv /usr/local/opt/selenium-server-standalone/*.plist ~/Library/LaunchAgents
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.selenium-server-standalone.plist
pip install selenium beautifulsoup4 argparse requests unidecode
```
## Usage ##
Sitemap should be standard SEO format.
```shell
python go.py --url "http://www.aruba.com/sitemap.xml" --output /Users/blitz/Downloads/aruba-screenshots
```