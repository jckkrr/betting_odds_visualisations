# Football betting odds visualisations
A graphical exploration of football betting odds, in order to see their predictiveness and discover insights into betting market inefficiencies.

The worksbook that uses four distinct graphical visualisations of football betting odds, from the 2019-20 German Bundesliga season, and discovers an insight about potential distortions in the betting market.

It begins by laying out the three types of odds for each match - home win, draw, away win - on a three-dimensional scatter plot.

![image](https://user-images.githubusercontent.com/69304112/209521180-ddf5d66f-09be-49be-8ad0-9c8765bceb76.png)

![image](https://user-images.githubusercontent.com/69304112/209736296-fd1faa75-9eac-4550-9812-af87f5a5b364.png)

![image](https://user-images.githubusercontent.com/69304112/209736585-d98e5494-ca33-4422-bfcc-6124d858f66c.png)

From this, it appears that the betting market is strongly predicitve of games at the extremes - and particularly the results of matches where the away team is the clear favourite. However, if you bet on all of these matches, would the occassions where this was not correct wipe out the slim winnings gained in the successes? To explore this, the next graph shows the return-on-investment when betting on every match up to a certain threshold: for example, betting on an away win in every match where the away team was paying less than 4.85 to win. On this (small) dataset, that returned an ROI of almost 19 per cent - a significant return that is worth exploring further. These returns were not seen in bets placed on home teams and draws, possibly suggesting gamblers undervalue an away team's ability to win on the road (or overestimate the home ground advantage).

![image](https://user-images.githubusercontent.com/69304112/209521311-0cd334ae-4e17-41c1-b520-f7c1def19053.png)

Could this profitability be enhanced by narrowing the window further and putting a lower limit of bets placed? This heatmap shows that that is possible, though in many of the most high-value windows, the pool of games is very small and therefore returns are vulnerable.

![image](https://user-images.githubusercontent.com/69304112/209734998-3c401769-8578-47f6-950f-d22b141ff7d6.png)

Looking at the distribution of odds for each team (either home or away) did not produce any insights.

![image](https://user-images.githubusercontent.com/69304112/209739408-ae11c8f4-5839-48fd-9472-794130935605.png)

Adapting this graph to look at results and odds per matchday, to see if the betting market became more efficient and better-predictive as the season progressed, indicated that their might a slight improvement in predicability with time - but only slightly, if at all. 

![image](https://user-images.githubusercontent.com/69304112/209739464-5eadd4ad-fade-4998-ba20-cfb3ee2a6937.png)

![image](https://user-images.githubusercontent.com/69304112/209739611-f12b55e6-e6b0-48ce-ab3b-7745991444fb.png)

In fact, the ROI on away wins can get as high as 40% if only bets were restricted to only matches in the second half of the season. This would reduce the pool of games available to bet on, though increase the likelihood of winning (again, this is based on just one season of data).

![image](https://user-images.githubusercontent.com/69304112/209743774-f1f7f462-b7cc-40b7-aefc-6c3f6aababaf.png)

The bar script was also adapted to look at the distribution of result types over the season. It produced a nice-looking chart though no discernible pattern emerged from it.

![image](https://user-images.githubusercontent.com/69304112/209739733-bba56598-7882-429e-8831-28067d2ba97d.png)
