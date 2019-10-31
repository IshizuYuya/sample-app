#!/bin/ash
tag=`cat sample-app-branch/.git/logs/refs/remotes/origin/HEAD | cut -d ' ' -f 2`
git clone sample-app-manifest changed-manifest
sed -i 's/sample-app:.*/sample-app:'${tag}'/g' changed-manifest/manifest.yml
cd changed-manifest
git config --global user.name "IshizuYuya"
git config --global user.email "Ishizu.Yuya@ap.MitsubishiElectric.co.jp"
git add -A
git commit -m "update manifest"