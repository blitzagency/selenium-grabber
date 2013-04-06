## Installation ##
```shell
brew install selenium-server-standalone  
ln -sfv /usr/local/opt/selenium-server-standalone/*.plist ~/Library/LaunchAgents
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.selenium-server-standalone.plist
pip install selenium beautifulsoup4 argparse requests unidecode
```
## Usage ##
Sitemap should be formatted as a line delimited list of absolute URLs.
```shell
python go.py <path_to_sitemap> <base_path> <image_output_path>
```
## Example ##
```shell
python go.py "/path/to/sitemap.txt" "http://www.google.com/" "/path/to/images/"
```
