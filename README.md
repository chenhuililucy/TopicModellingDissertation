





 **Using Categorical Data to Facilitate Learning for Financial Disclosures**

**Applications of the Attribution Dictionary**

Chenhui (Lucy) Li

_Said Business School_

_University of Oxford_

Date

- **Abstract**

This paper discusses the application of the sentiment dictionary which I have jointly developed with Aaron Aujla to analyze the content of management discussion. In the first section of this paper. I demonstrate the relevance of our dictionary with use of topic modelling methods (latent dirichlet allocation and cosine similarities) and study the implications of topic discussion in both a strategic management context and an empirical finance context. I explain the reasons behind my findings with and co-movements of subtopics with fundamental and market based indicators. In the second section of this paper, I explore the joint use of this dictionary with supervised machine learning techniques. Overall, this paper intends a complete analysis workflow focusing on combining the web of dictionaries with machine learning applications to provide guidance to future research in the area of topic modelling within empirical finance.

# Add implications to management

**WIP**![](RackMultipart20201220-4-1xcaf2u_html_ef361b03758004a7.png)

# **1**

#

# **Introduction**

#

Advances in computing has made the analysis of textual data increasingly tractable. In finance, recent studies have addressed how financial markets respond to the language in newspaper articles (Tetlock, 2007; Tetlock, Saar-Tsechansky &amp; Macskassy, 2008), earnings reports (Loughran &amp; McDonald, 2011), and various types of regulatory disclosures (Hanley &amp; Hoberg, 2012). However, the NLP technology used in firm performance/stock price prediction is nascent. The most influential studies in this area are Tetlock (2007) and Loughran and McDonald (2011). They evaluate sentiment by weighting terms based on a pre-specified sentiment dictionary and summing sentiment scores. A smaller volume of research also uses textual data to infer information on strategic management or organizational behaviour perspective and observe the relation between current disclosure and future firm performance. The textual data used for these studies were often obtained through manually encoded texts.

Nevertheless, there are various issues associated with each of these methods. Existing sentiment dictionaries capture polarity (for instance, how positive/negative a firm&#39;s filing is) but not context (the subject matter the firm is feeling optimistic/pessimistic about). Manual labelling has the downside of human errors and sample size restriction, papers using this method usually less than 100 companies and across a maximum of five years, as researchers must manually search through the texts. No research thus far has looked into creating a standard workflow that can be replicated in future studies.

There are multiple problems in past literature&#39;s estimation strategies. On a high level, the common issue lies in the fact that each fails to account for different unobserved features of financial text. I argue that caveats of previous analysis methods lies in the following:

1. Existing NLP toolkits only allow for accurate stock prediction (eg. abnormal returns) but not predictive performance (eg. future ROA, revenue) because no techniques can proxy for discussion of firm decision making, firm actions and thought process at the same as an evaluation of firm performance.

1. Past research controlled for insufficient characteristics within firm&#39;s textual disclosures.

This paper serves to bridge this gap by combining financial dictionaries and unsupervised machine learning to create a automated text analysis workflow so that future researchers can replicate in order to form a predictive model for future firm performance. I account for the following factors to arrive at a predictive model:

1. Disclosure on features internal or external to the firm, understanding the implications of specific organizational efforts (eg. &quot;strategic acquisition&quot;, &quot;superior management&quot;) on financial performance. Most literature relating to this analysis involved manual encoding There are currently no academic literature that worked on quantifying these features. I make this possible by utilizing a relational dictionary I and others created.
2. Whether discussion on financial performance (eg. &quot;increase in revenue&quot;) leads to actual superior performance in the future for a firm
3. High level textual characteristics (eg. regulatory/compliance discussion, investments, securities and derivatives)
4. To instrument the above discussion by controlling for the sector/industry of the business

![](RackMultipart20201220-4-1xcaf2u_html_7a1280c116ef1156.png)

Figure 1. Proposed Prediction Model

The textual data used in this paper comes from 80,000 MD&amp;A (management discussion and analysis) sections of firms&#39; disclosure. Located in companies&#39; 10-Ks, MD&amp;A is written to give the investor an opportunity to look at the company through the eyes of management by providing both a short and long-term analysis of the business of the company. Yet, given that the very purpose of the MD&amp;A is focused on justifying performance with strategy/actions taken by the firm, it is important for a researcher to associate rationales behind performance with the firm&#39;s actual performance.

This paper begins by evaluating current methods of NLP in the industry and related background research. The empirical section of this paper is divided into two sections. First, I deploy topic modelling techniques to study the evolution of MD&amp;A disclosure content overtime and the reasons behind this. Similar to Dyer et al. (2016), I make the observation that readily observable firm characteristics or non-textual characteristics do not sufficiently explain the trends in MD&amp;A vocabulary, thereby supporting my construction of the prediction model. I subsequently explain how I arrived at the prediction model. I explain the strategic management literature that inspired the web of dictionaries used to proxy for financial performance and organizational factors, then, I proceed on to explain document topic modelling.

# **2**

#

# **Theoretical background**

Research on predictive performance is rather limited compared to research on stock returns. Past NLP research utilized pre-determined dictionaries, or supervised machine learning to assess disclosure characteristics (e.g., uncertainty, positive/negative tone) based on human defined classification themes. Others studies used unsupervised learning methods to associate measures of readability, similarity, deception, or length with firm fundamentals.

In this section I introduce tools for textual analysis and their applications to modern NLP financial applications. I describe the use of machine learning methods and dictionary methods deployed in past literature to perform sentiment analysis on financial text.

![](RackMultipart20201220-4-1xcaf2u_html_9037bb3d4d7eb150.png)

Figure 2. Common NLP methods at present

**2.1 Machine Learning Methods**

Machine learning methods in the financial NLP field can be grossly categorized into two categories: supervised and unsupervised approaches. In the context of financial NLP, supervised learning requires a labeled dataset, whilst unsupervised machine learning looks for previously undetected patterns in data with no existing labels. Supervised machine learning is used for text classification (ie. deciphering whether a sentence/document conveys positive/negative sentiment), whereas unsupervised machine learning is used for topic modelling, categorizing documents with respect to the topics discussed within them or extracting (latent) topics from texts.

**2.1.1 Supervised Sentiment Analysis in stock price prediction**

The efficient market hypothesis stipulates that investors consider all available information in their decision making process (Fama, Fisher, Jensen &amp; Roll,1969; Fama 1970). Market efficiency implies that any news, once released into the market, will be immediately assimilated into prices. Yet, empirical evidence from natural language processing (NLP) uncontroversially supports the contrary argument that information contained in financial market events is predictive of future asset price paths. The application of NLP in stock price prediction is still nascent compared to other fields, and remains predominantly focused on analyzing sentiments in financial disclosures at the word-level.

Supervised sentiment analysis uses a set of training documents, classified into a set of predefined categories, to generate a statistical model that can be used to classify any number of new unclassified document. Sentiment scores are then used in a secondary statistical model for investigating phenomena such as stock returns in financial markets (Tetlock, 2014). Nevertheless, a critical issue in this field is the lack of classified textual data. A few research agendas seek to bridge this gap: Malo et al. (2014) trained classifiers to conduct sentence-level semantic analysis for financial news and provided a Financial Phrase Bank consisting of a set of 5,000 sentences, manually annotated by 16 subject experts. This resource was updated by Sinha et al. (2019), who also released an entity-annotated news dataset containing over 12,000 headlines and their related financial sentiment. Oliveira et al. (2016) produced a stock market sentiment lexicon, which includes 20,551 items extracted automatically from microblogs (StockTwits and Twitter). However, building a model based solely on these existing data sets is inadequate for two reasons. First, all existing labelled dataset are classified based on polarity, this makes supervised sentiment analysis more applicable to stock price forecasting than predictive performance. Stock prices are highly sensitive to public sentiment but firm performance is down to miscellaneous factors (eg. management). Polarity of news/financial filings may be an effective proxy of public sentiment but less so of the components leading to firm performance because it is more about how decision making of the firm leads to long run impact. Second, in the process of producing a labeled dataset, annotators reviewing financial text would assign a positive/negative tag to isolated sentences. Yet, in an actual news event, some positive/negative textual description may already assimilated into prices and others might not, thus amplifying the problem of ambiguous causality. For example, prices of stock X may already reflect the fact that numerous articles hypothesize that stock X might fall. The ambiguity in the textual context hinders the predictability of the model. As a means of disambiguation, it would be preferable if documents are labelled based on multiple features instead (eg. certainty, financial content, etc). Gathering labelled data for the task is strenuous and requires the expertise of financial analysts. At present, there is no available tagged dataset for feature engineering.

Additionally, machine learning approaches to sentiment analysis are subject to criticism due to their lack of transparency: Most supervised machine learning utilizes methods such as Naïve Bayes (Antweiler and Frank, 2004), LSTM networks (Maia et al, 2018) and neural networks (Kraus and Feuerriegel, 2017). All of these methods use thousands of unpublished rules and filters to measure the context of documents, and hence are opaque and difficult to replicate.

An alternative solution researchers developed is to use stock returns to screen for sentiment charged words, and use those sentiment words as the labelled dataset. Ke et al (2019) designed a workflow that could screen for sentiment charged words based on their cooccurrences with stocks of high/low returns, assigning sentiment weights to these words and scoring documents with a multinomial mixture model based on the frequency of sentiment charged words. However, this method would still fail to capture the nuisance of the financial language, as it is still a &quot;bag of words&quot; model that does not take into account the importance of syntax. It does not account for negation, hence unable to distinguish between &quot;decrease in debt&quot; and &quot;increase in debt&quot;. Additionally, the classification algorithm would not pick up phrases, as it only uses single word tokens.

In this paper, I choose not to adopt a pre labelled dataset and to utilize the aforementioned forms of supervised machine learning. It would not be possible to rectify the problems inherent to the technique and the datasets. I also recognize that new patterns would emerge in future texts and lessening the predictability of currently available pre labelled texts.

**2.1.2 Latent Dirichlet Allocation in Topic Modelling**

Topic modelling can be described as a method for finding a group of words from a collection of documents that best represent the information in the collection. It is an indispensable toolkit to arrive at contextual information from text documents. Before the advent of topic modelling in machine learning, researchers relied on manual classifications to control for the differences between documents. Boudoukh et al. (2013) use an ex ante list of 14 predefined categories (such as &quot;acquisition, deal, legal or award&quot;) to differentiate between relevant news for companies to study the impact of news on abnormal stock return. This is similar to the method adopted by Neuhierl et al. (2013), who manually classify press releases into major news categories and their subcategories based on content, 10 major news categories, further subdivided into 60 subcategories. Gooding and Trisboe (2019) used paid data from All Street Research, containing 3097 instances, with categories defined by analysts which they narrowed down to 1824 examples and 11 categories. This study suffered from a small sample size: several categories containing less than 100 examples which meant that they were not enough to train and test.

Later research shows further integration of topic modelling with machine learning methods, especially Latent Dirichlet Allocation (LDA), an unsupervised machine learning algorithm aiding researchers to extract a number of predefined topics from a collection of financial text. Researchers define the number of topics they seek to extract, and the algorithm finds the most likely choices for these topics and output them in terms of word vectors. Past research has focused on using LDA to distill core properties of disclosure. Studies have focused on using LDA to predict currency fluctuations, equity returns and examining validity and truthfulness of corporate disclosures. LDA also allowed topic modelling to be scaled to large samples.

![](RackMultipart20201220-4-1xcaf2u_html_c7e362c7aa7b8b8e.png)

Figure 3. Summary of LDA literature and their contributions at present

One of the downsides to LDA is the occasional lack of human interpretability and spurious results, often due to the complex nature of financial language. Computationally distinguishing between topics referring to &quot;firm inherent competencies&quot; and &quot;changes enabled by management&quot; using a statistical model is far more difficult than distinguishing between documents referring to &quot;music&quot; and &quot;animals&quot;, because, in the case of the former, there are far more words that co-occur in both contexts. Hence, LDA would fail to precisely account for all existing topics. However, this problem would be rectified if these potential topics are further categorized with human efforts. This is what I will attempt to do in the empirical analysis of this paper: I describe how using a relational dictionary may be used to capture this information.

**2.2**  **Dictionary Methods**

As opposed to machine learning methods, dictionary based methods have the benefits of being friendly to the exercise of human backtesting. Dictionaries are word lists grouped into categories, with each category defined by its associated attributes, used to assign tags to financial texts, as a result of the tagged textual document predictions on stock returns can be made.

Figure 4 . ![](RackMultipart20201220-4-1xcaf2u_html_8bb05a1e02919881.png)

Past dictionaries were created to classify the tone of the documents. The studies pre-dating the paper have almost exclusively relied on generic dictionaries. Tetlock (2007) was among the first to demonstrate the benefits of using the Harvard General Inquirer, a less sophisticated sentiment analysis dictionary developed for use in more general contexts, in a financial context. There are also other variants which use a combination of heuristics, WORDS (e.g. Frazier et al., 1984), Diction or Wordstat to perform dictionary-based searches for sentiment cues (Demers &amp; Vega, 2008; Davis, Piger, &amp; Sedor, 2007). The most widely used a finance specific sentiment dictionary to date is created by Loughran and McDonald (2011). Their main contribution is to point out that many words that have a negative connotation in other contexts, like tax, cost, crude (oil) or cancer, may have a positive connotation in earning reports. For example, a healthcare company may mention cancer often and oil companies are likely to discuss crude extensively. Loughran and McDonald (2011) conclude that as much as 73.8 percent of Harvard General Enquirer&#39;s negative words do not have a negative sense in financial documents. To this date, Loughran and McDonald dictionary is the most popular dictionary used in a financial context due to its simplicity and clarity. The dictionary consists of words grouped into multiple categories, such as &#39;neg&#39;, &#39;pos&#39;, &#39;uncertain&#39;, &#39;litigious&#39; and &#39;constraining&#39;. Entries under each category are in the form of a single word and their possible inflections (eg. loss, losses, lossed)

However, the LM dictionary may still yield biased results. Firstly, it covers only unigrams (single-word dictionary entries) and ignores the subject described. I seek to build on the LM dictionary by developing a more sophisticated lexicon consisting of both unigrams and bigrams (single-word and two-word phrases). For instance, using the LM dictionary, we would classify an improvement in economic condition or refinement of company strategy as positive factors. The former is entirely out of the control of the firm whereas the latter is the result of actions taken deliberately by the firm. It may well be that the improvement in economic condition is well known and priced in whereas opinions on actions taken by the firm is not. Hence, only the latter may be of material use to analysts. The LM dictionary also fails to capture descriptions of performance outcomes such as &quot;increased revenue&quot; (positive) and &quot;decreased cost&quot; (negative) because &quot;increased&quot; and &quot;decreased&quot; are classified as neutral.

# **3**

# **Estimating Topics**

**3.1**  **Document information proxies**

Before constructing the model, it is vital to proxy for what information we are looking to infer from textual data and how this might have implications on corporate performance. I incorporate the following variables into the prediction model and use a best subset regression to proxy for the best variables to the prediction problem.

Firstly, we need to account for a firms&#39; current performance, as it may be correlated with future performance. It may be that some form of mean reverting behaviour exists and firms having filings with positive performance may experience a decline in performance in the longer run.

Second, I proxy for the multiple dimensions of the firm&#39;s strategies that are critical to a firm&#39;s building of competitive advantage. In prominent strategic management literature, there are three complementary views: positional, resource based and value system.

- **The positional view**

Porter (1979)&#39;s theories are at the forefront of the positional approach, he described strategy as &quot;building defenses against competitive forces or finding positions in the industry where the forces are the weakest&quot;. The prescriptive value in understanding and applying the &quot;Five Forces Analysis&quot; lies in positioning a firm in a way such that it is less vulnerable to attack within the industry. The technique Porter designed identifies the potential for a firm in making profit in the industry and determining competitive intensity or industry attractiveness.

![](RackMultipart20201220-4-1xcaf2u_html_1ea907eff6bcec50.png)

Figure 5 .

- **The resource based view**

The resource based view has a much stronger focus on the internal resources of the firm, which can be defined as the &quot; tangible and intangible assets a firm uses to choose and implement its strategies&quot; (Barney, 2001). These assets come together to shape the key capabilities of a company, through which the company archives a sustained, competitive advantage by leveraging unique firm resources that highly impact its strategy. Companies hold resources that differ across four parameters: value, rareness, imitability, and substitutability, and if a company &quot;discovers&quot; a particular set of unique resources that directly impact its strategy, it is capable of realizing competitive advantage that cannot be replicated by competitors.

- **Value system**

Porter&#39;s value chain focuses on systems, and how inputs are changed into outputs purchased by consumers. He describes a value chain common to all businesses, that he divides into primary (relating to the primary, sale and support of a service) and supporting activities. Primary activities relate directly to the physical creation, sale, maintenance and support of a product or service (eg. inbound/outbound logistics, operations, marketing/sales). Support activities relate to technological development, infrastructure, human resource management and procurement. Understanding of the value chain could be used by firms to find opportunities to increase value.

![](RackMultipart20201220-4-1xcaf2u_html_c1b9560fb6561cbd.png)

Figure 6 .

Nevertheless, on a textual basis, it may be difficult to differentiate between the strategy dimensions (especially between the resource based view and Porter&#39;s value system) at a high level just because there are multiple areas of overlap in terms of vocabulary. For example, superior technology may be discussed as a resource in RBV and as part of the support activities in Porter&#39;s value chain. Additionally, it is rather difficult to distinguish between activities in similar categories (eg. between inbound logistics and outbound logistics). In order to incorporate all characteristics of the aforementioned, but at the same time sufficiently differentiate between distinct categories, I choose to regroup strategic discussions into the following categories:

![](RackMultipart20201220-4-1xcaf2u_html_b7ce72c94418134e.png)

Figure 7 .

The internal category consists of textual measures that account for firm competency (in alignment with the resource-based-view), and various stages at a firm&#39;s strategic management process (Barney, 2011): from decision making to actions to results realization. Each of the steps in the process would correspond to certain firm activities in Porter&#39;s value system. The external category consists of Porter&#39;s Five Forces and economic, institutional forces that firms discuss.

Aside from strategic discussions, I would also like to collect data on the associated qualifications in terms of sentiment or performance results as a consequence of these strategies. I measure the degree of firms&#39; responsibility taking (if any). Firms may wish to attribute performance to internal/external reasons. In past literature, firms tend to attribute positive results to internal causes while attributing negative performance to the external environment to take credit for successes and avoid blame for failures (Miller and Ross, 1975; Schlenker, 1980). The directionality of attribution is indicative of future performance. It is widely posited that attributions are likely to be &quot;self-serving&quot;. Previous finance research used textual data in corporate reports to analyse the relationship between textual attribution and performance. Staw et al. (1983) and Salancik and Meindl (1984) find that positive sentiment expressed in corporate annual reports is usually correlated with poor future performance. Bowman (1976) finds that more successful firms place emphasis on their own strategies and less successful firms blame on external excuses (ie. weather) in their annual reports. Firms that tend to be more optimistic in their disclosure (disclosure of positive revenue increase, etc), may experience worse performance in the future.

**3.2**  **Empirical model**

Our overall econometrics specification estimates the overall effect of disclosure measures on the financial performance, which I proxy with ROA. I use a pooled model where data from different units of our independent variables are pooled together with no assumption on individual differences. (Test First)

The empirical model may be formulated in the following form:

In the empirical model, , , and are independent variables that describe the characteristics of the textual disclosures and the rest are control variables that describe the characteristics of the firm.

| Variable | Variable Description |
| --- | --- |
|
 | Metric accounts for texts that convey strategic content classified as &quot;internal&quot; in _fig. 7_, without any attribution to performance. It intends to measure the quantity of discussion, and not the favorability.
Example sentence:
 &quot;_We pursue a strategy of supplementing internal growth by acquiring other financial companies or their assets and liabilities.&quot;_
Sentence falls under the _&quot;firm action&quot;_ category, and illustrates the means by which the firm seeks to achieve its strategy.
 |
| | Metric accounts for texts that convey strategic content classified as &quot;external&quot; in _fig. 7_, without any attribution to performance. It intends to measure the quantity of discussion, and not the favorability.
Example sentence: &quot;_Under the authority of eesa, treasury instituted the tarp capital purchase program to encourage u.s. financial institutions to build capital to increase the flow of financing to u.s. businesses and consumers and to support the u.s. economy. &quot;_
Sentence falls under the _&quot;economic, institutional reasons&quot;_ category, as it is an example of how the firm reacts to external forces in its environment.
 |
|
 | Metric accounts for texts that convey strategic content classified as &quot;internal&quot; in _fig. 7_, with some to performance. It intends to measure the polarity/favorability of the discussion (whether a positive, or negative performance outcome is attributed to strategic discussion).
Example sentence:&quot;_The decrease in gross profit as a percentage of sales for 2014 as compared with 2013 and for 2013 as compared with 2012 was primarily due to increases in promotional activity and product cost increases, some of which were not passed on to customers.&quot;_
Sentence falls under the _&quot;firm action&quot;_ category and attributes negative performance _&quot;a decrease in gross profit&quot;_ to firm action. |
|
 | Metric accounts for texts that convey strategic content classified as &quot;external&quot; in _fig. 7_, with some to performance. It intends to measure the polarity/favorability of the discussion (whether a positive, or negative performance outcome is attributed to strategic discussion).
Example sentence in sample:&quot;_These loans may therefore be more adversely affected by conditions in real estate markets or in the economy in general.&quot;_
Sentence falls under the _&quot;economic, institutional reasons&quot;_ category, and attributes worse performance as a result of _&quot; loans&quot;_ to the economic conditions. |
|
 | Return on assets (Net Income/Revenue) х (Revenue/Average Total Assets) is used as a common indicator of firm performance, commonly used as a proxy for for evaluating firm performance (Edward et al., 1976; Aerts, 2001) |
|
 | Number of business segments, used as a proxy for the size of the firm. Empirical evidence suggests different evidence on how firm size affects growth in firms&#39; financial performance: Gibrat&#39;s Law states that the expected increase in firm growth is proportional to its size, Bentzen et al. (2011) finds that firm&#39;s growth rates are more likely to be positively related to firm size.
 |
|
 | Disclosure length of the MD&amp;A section, controlled for as it may influence the proportion of internal/external discussion. |

|
 |
Leverage (total debt to total asset ratio) is indicative of a firm&#39;s ability to meet its financial obligations. The majority of conducted empirical studies find a negative relationship between company returns and leverage. Baker (1973) examined the effects of financial leverage on industry profitability and concluded that firms who earned systematically higher returns had a relatively low degree of leverage.
There are numerous different theories on the optimisation of firms&#39; capital structure. Modigliani and Miller (1958) presented a proposition that highlights the irrelevance of capital structure. Another well known theory is the pecking-order theory (Myers &amp; Majluf, 1984), which states that firms prefer internal financing to fund their operations. The trade-off theory, in contrast to the pecking-order theory, suggests that firms can reach an optimal level of leverage, in which the benefits of tax shields are directly offset by costs from financing distress (Kraus &amp; Litzenberger, 1973; Myers, 1984). The theories mentioned also imply that certain relationships between leverage and profitability are expected, endorsing a non-zero coefficient on leverage.
 |
| --- | --- |
|
 | Market capitalization is an important market indicator of the value of shares, otherwise the value of companies in general (Toramane et al., 2009; Dias 2013). Empirically, Donaldson (2015) finds a significant positive correlation between firms&#39; ROA and market capitalisation. |

Based on the nature of the variables included within the regression, and from my previous hypothesis, I hypothecate the following about the parameters.

- \&lt; 0 : as attributing negative performance to internal reasons likely correlate with improved future performance
- as a display of more strategic awareness focusing on the internal of the organization likely correlate with with improved future performance
- : wherein as a display of more (positioning) strategic awareness (Porter&#39;s 5 Forces) likely correlate with with improved future performance
- \&lt; 0: as attributing negative performance to external reasons likely correlate with improved future performance
- ≤ 0: by Modigliani and Miller (1958) and Myers &amp; Majluf (1984), higher leverage likely affects future performance in a neutral or negative way.
- \&gt; 0: by empirical evidence, market capitalization is positively correlated with ROA.

**3.1**  **Sample Selection and Construction**

The management discussion and analysis section (MD&amp;A) in corporate 10-Ks is one of the most read and important components of the financial statements. Most literature find a significant correlation between current fundamentals and market reactions and textual disclosures.

In 1995, safe harbour provisions of the private securities and litigation reform act encouraged more forward looking information and should make MD&amp;A more informative. On the other hand, the MD&amp;A may not present accurate information because it is not required to be audited. (Hufner, 2007) .

I webscrape 10-K filings filed electronically with the SEC on EDGAR from 1993 to 2018. This yields 149,139 10-K and 10-K405 filings from which we were able to parse the Management&#39;s Discussion and Analysis. Management&#39;s Discussion and Analysis comprises Item 7, which usually describes the results of operations, internal and external factors relevant to the business&#39; performance, and Item 7A, Qualitative and Quantitative disclosures about Market Risks. I have excluded 10-K-A from our sample and eliminated disclosures that contain fewer than 1000 characters, which are disclosures without material information or disclosures that have MD&amp;A section incorporated by reference to the annual report (usually incorporated into exhibit 13, which is kept as a separate file to the main 10-K filing on SEC Edgar). In the latter case, similar to Loughran and McDonald (2011), I find that the beginning and ending positions of the MD&amp;A document when filed in an exhibit are not demarcated in a manner that facilitates accurate parsing. Aside from the MD&amp;A section, exhibit 13 often contains financial statements, notes, as well as the auditor&#39;s report, all of which is irrelevant for the purpose of my exercise.

The matching algorithm is designed to capture the position of &quot;item 7. management&#39;s discussion and analysis&quot; and &quot;item 8. consolidated /audited financial statements&quot; and extract the text in between when it satisfies certain heuristics. I remove all numbers and numerical tables, keeping only the text. We identified 87,834 MD&amp;A sections that fulfill this requirement.

I subsequently perform several processing steps that are common in text mining (Manning and Shütze, 1999). I transform the running text into a matrix notation that would allow for further calculations with Scikitlearn&#39;s vectorizer. First of all, I remove stop words that frequently occur in the English language. I use the default NLTK&#39;s list of English stop words which consists of common, short function words that do not add additional meanings to our text - examples of these are conjunctions and pronouns such as &quot;ourselves&quot;, &quot;her&quot;, and &quot;between&quot;.

**3.2**  **Initial Topic Modelling**

First, I would like to extract high level features and interpret what these statistical results mean in a managerial context with unsupervised machine learning. I analyze the evolution of topics using LDA (Blei, 2011) . LDA is a robust method that relies on statistical correlations among words in a large set of documents, it is a dimensionality-reduction technique, similar to principal components analysis, which transform high dimensional textual data to low dimensional data. The fundamental challenge with any NLP procedure is that raw text suffers from the curse of dimensionality, which makes it computationally intractable. LDA would allow me to explicitly identify and empirically quantify the low-dimensional representation so that it retains meaningful properties of the texts. More information on the statistical definition of the method and the codes can be found in the appendix as I avoid excessive mathematical explanations.

**3.2.1 Topic length evolution**

The first set of empirical results I show aims to study the changes in topic distributions over time. Dyer (2017) studied the evolution of the changes in length of topics on whole 10-Ks. However, no up to date research has been done on MD&amp;A. Given that the content in the MD&amp;A confers the most amount of information from a corporate strategy standpoint, I hypothesize that results from running LDA over the MD&amp;A will differ meaningfully from Dyer (2017). I replicate Dyer (2017) to study the evolution of length of disclosure for MD&amp;As instead.

I first used LDA to output 25 clusters from the set of MD&amp;A documents. I then assigned each document to their most probable cluster and collected the length of MD&amp;A documents for each topic across the time frame of 1993-2018. For each topic, I compute the median length of all of its associated documents in each year and plot the observations graphically (see figure 6.). I show in a tabular form the broad clusters in which I group the computer generated clusters from LDA (see table 1). In general, clusters fall under two major categories: sector-specific (upper table) and business/operations specific (lower table). For sector-specific clusters, only the most prominent sectors by US GDP (eg. finance, real estate, oil and gas, healthcare) having the most distinctive vocabulary (eg. &quot;futures&quot;, &quot;mortgage&quot;, &quot;oil&quot;, &quot;drug&quot;) are clearly demarcated by the algorithm. For business/operations specific clusters, the output of LDA insufficiently distinguishes between the aforementioned strategies dimensions I previously mentioned. The boundaries between several clusters appear murky (eg. Operations Financials) with many clusters having the same vocabulary.

![](RackMultipart20201220-4-1xcaf2u_html_62cc148fdbc4c888.png)Figure 6 .

![](RackMultipart20201220-4-1xcaf2u_html_7a424d48273e3f07.png)

![](RackMultipart20201220-4-1xcaf2u_html_a00e8c31537ab946.png)

Table 1.

Dyer (2016) faced the same lack of clarity between clusters: he observed that numerous topics could be classified into the same category. He resorted to grouping topics from LDA into further categories. He makes the observation that the disaggregation of the overall trend in length into the portions attributable to individual types of disclosure. However, Dyer (2016)&#39;s paper has several caveats: first, because the paper relies on only using LDA to study the content of 10-Ks, which suffers from boundary ambiguity, it insufficiently captures a complete picture of disclosure. Second, it does not test the informativeness of the textual attributes measured. I will proceed to suggest solutions in the second part of the empirical section of the paper.

Looking at the first stage results obtained, a general trend is evident: disclosure length has become longer overtime across all topics (though not necessarily increasing across all years). This observation is different from that of Dyer et al (2016), who, after conducting the same analysis on the whole sample of 10-Ks, found that only documents pertaining to compliance with SEC &amp; accounting standards which increased markedly in the sample period. The finding aligns with Dechow et al.(2010), who observed that, with increasing MD&amp;A length, managers increasingly use boilerplate disclosure (ie. standard disclosure that uses many words with little firm-specific content). As the lack of concision of MD&amp;A may reduce the value of the information MD&amp;As provide, the need to arrive at an automated way to identify essential information becomes much more essential.

Additionally, most of the clusters that experience slow growth in length overtime (eg. cluster 0, cluster 11, cluster 14) relate to revenue, cash, and operating financials (although cluster 9 is an outlier). These clusters are less analytical and focus on describing material performance. In contrary, cluster 18 (products, services, customers) and cluster 13 (decision making, evaluation) experiences more fluctuations. This tells us that much of the increase in overall MD&amp;A length can be explained by the addition of more strategic content, rather than descriptive content.

Thirdly, amongst all 25 clusters, the cluster relating to environmental concerns experienced the most dramatic increase. ESG has become a quintessential part of corporate disclosure overtime. The Sustainability Accounting Standard Board (SASB) was established in 2011 to develop standards for companies to make comparable, consistent, comparable and reliable disclosure about sustainability or ESG matters. The increase in disclosure length on environmental concerns certainly demonstrates progress in a regulatory sense. Nevertheless, it is unclear if firms simply expressed &quot;boilerplate&quot; ESG concerns or have acted upon them: thus, information from LDA is insufficient to tell us if firms that disclose more ESG content are likely to witness improved performance. In parallel with the O&#39;Donovan (2002), firms may be using specific micro-tactics dependent on whether the purpose of the response is designed to gain, maintain or repair a firm&#39;s environmental legitimacy (that is, to act within the bounds of what society identifies as socially acceptable behaviour). In the subsequent part of this paper, I discuss the correlation between more environmental disclosure and firms&#39; performance.

Lastly, discussion clusters exhibit different degrees of cyclicality. In the event of a financial crisis, the length of topics relating to the external economy and debt increases whilst those relating to internal operations decline. For example, cluster 2 (securities), 3 (corporate borrowing) , 6 (real estate) , 20 (derivatives, trading) have seen the most increase in length post financial crisis (2018-2019). On the other hand, cluster 9 (operations financials) and 16 (valuations) have seen the most significant decline in length. An explanation can be made on the basis of the attribution theory: firms tend to attribute good news to own superior management and bad news to external reasons. Given that the financial crisis is a systems wide event, firms would likely shorten the discussion of poor operational performance and describe the crisis in great detail.

**3.2.2 Emergence of New Topics**

The study on topic length evolution reveals interesting cross sectional characteristics of MD&amp;A texts. Subsequently, I analyze the emergence of new topics over time. Previously, I have computed LDA by selecting 25 topics over the whole duration of 25 years, in this part of the analysis, I instead use LDA to select the most prominent 25 topics in each year, and compute the topic that has the most different content with respect to the 25 topics in previous year.

As the topics calculated by the LDA model are a vectorised representation of words, it is possible to calculate how similar they are with the use of cosine similarities, defined as the degree of similarity between two sparse vectors. The algorithm first extracts the top 1000 words that are most probably assigned to the respective topic, outputs these words in vector form. Subsequently, the sum of the dot products of these vectors is computed and the result is normalized by the multiple of the magnitudes of these vectors (see Figure 7). For each year, I compute a rolling set of cosine similarity calculations by comparing each topic with every topic in the previous year. I take the mean of the former and finds the topic with the smallest mean (least similar to all the topics in the previous year).

![](RackMultipart20201220-4-1xcaf2u_html_1da0a402f2707934.png)

Figure 7 .

![](RackMultipart20201220-4-1xcaf2u_html_e5ca6920b754b376.png)

Figure 8 .

For a pictorial illustration of cosine similarities (see Figure 8), we seek to minimize in the diagram (or similarly, to maximize given its bounds: 0\&lt;\&lt;180) , with &#39;item 1&#39; and &#39;item 2&#39; being word vectors respectively of 1000 length, from year t-1 and year 1 respectively.

Table 2. shows the resulting topics each year from the analysis with the lowest cosine similarity with all previous years. I grossly categorized topics into the following categories:

- **Orange** : global macroeconomic event
- **Yellow** : regional macroeconomic event
- **Green** : macroeconomic trend
- **Blue** : management related

![](RackMultipart20201220-4-1xcaf2u_html_5783a0f949694adc.png)

Table 2.

First, it is apparent that the time series study captures mostly macroeconomic clusters. The 1995 reference to &quot;peso&quot; and &quot;bankruptcy&quot; relates to the Mexican peso crisis where the Mexican government was forced to devalue the peso against the US dollar. The period 2007-2010 see financial description that relates to the global financial crisis, with trading ideas being prominent in 2007 and sentiment becoming increasingly bleak in 2009. The clusters also capture macroeconomic factors that were not as internationally known: the reduction of supply and peak in oil price in 1996, Enron&#39;s collapse in 2001, as well as the decommissioning of the Yankee power station in 2004. Several of the clusters also exhibit macroeconomic trends: advancement of new energy in 1997, the dot com bubble in the early 2000s, and the growth of environmentalism in the early 2010s.

Comparatively few topics relate to changes in management practice, highlighted in blue. It is comparatively hard to provide reasons for why these topics emerged during the time when they did. Whilst LDA adequately captures system wide shock and the sectors that experience the most dramatic change overtime (eg. software, new energy), it is rather difficult use LDA to capture changes relating to management related disclosure (eg. strategy-relevant content). In the mid 2010-late 2010s, although there are This may be problematic in fact

**2.2.1 The Internal/External and Performance Dictionaries**

**Fig 1: Dictionary Composition.**

Our positive/negative performance dictionary consists of 5 sub dictionaries and internal/external dictionary consists of 2 sub dictionaries.

![](RackMultipart20201220-4-1xcaf2u_html_80d85e481243aa6d.png)

**Fig 2: Relationship between individual dictionaries**

Performance phrases are formed by joining amplifier/negator/bads with positive/negative tokens, a performance phrase consist of 2-3 words. Phrases in our internal/external dictionary consist of 1-2 words each.

![](RackMultipart20201220-4-1xcaf2u_html_c453664ae555b558.png)

The dictionary consists of two parts: an internal/external dictionary featuring key terms justifying business performance, and a performance dictionary consisting of amplifiers, negators, bads, positive and negative performance vocabulary.

**2.2.1 The Performance Dictionaries**

An &quot;amplifier&quot; enhances the polarity of the finance specific vocabulary that it is attached to (eg. increased, enhanced, booms, surges, acquire, retain, etc), most amplifiers we have selected are unigrams. A &quot;negator&quot; negates the polarity of the finance specific vocabulary that it is attached to (eg. decreased, reduces, etc). Word in the &quot;bad&quot; category directly makes the polarity of the finance specific vocabulary negative (eg. adverse, constrains, etc).

The positive performance dictionary consists of financial performance tokens and business activities that when amplified, benefits the business (eg. revenue, sales, income, acquisition asset) Conversely, the negative performance dictionary consists of financial performance tokens and business activities that when amplified, negatively affects the business (eg. costs, risks)

The positive and negative performance dictionary consist of financial performance tokens, we have included tokens that have a unique meaning. For instance, &quot;accounting cost&quot; is not incorporated as &quot;costs&quot; is in our dictionary and &quot;accounting&quot; does not add an additional layer of meaning to &quot;cost&quot;. For the same reasons, keeping&quot;amortization certain&quot; is not meaningful because &quot;certain&quot; does not add to &quot;amortization&quot;. &quot;Advertising budget&quot; is not included as &quot;advertising&quot; does not add to the polarity of &quot;budget&quot;. However, &quot;Debt maturities&quot; is relevant because both debt and maturity are significant to the polarity of the phrase &quot;Expense reimbursements&quot; is relevant because reimbursement alters the meaning of expense.

**2.2.1 The Internal Dictionary**

Phrases in the **internal dictionary** are defined to fall under any one or more of the following categories.

**Category I: Firm decision making:** the maintaining/altering of management decisions/actions or evaluation of management/managerial intentions, such as investment into research and development, discussion about opportunities. Decision making is central to the development of firm strategy. Porter (1996) states that the role of strategy is to define position, determine trade-offs and forge fit among activities. More discussion on decision making would be correlated with positive gains on future performance. &quot;Designing&quot; strategy is a prevalent school of thought in the field of strategic management. Mintzberg (1990)&#39;s design school of strategy posits that strategy is a process of design to achieve an essential fit between external threat, opportunities and internal distinctive competence. Yet, the converse may also be argued: a company&#39;s choice to enter a new position makes sense only if it has the ability to system of complementary activities into sustainable advantage.

_Table 1. Key Tokens and Associated Bigrams identifying phrases in the &quot;Firm decision making&quot; segment of the dictionaries._

| **Key Unigram Token and Associated Bigrams** | **Dictionary Unigram/Bigram Frequency** |
| --- | --- |
| Competitive (eg. Competitive Strength) | 252 |
| Achieve (eg. Transaction Achieved) | 287 |
| Solution (eg. Solutions Provided) | 631 |
| Judgement |
 |

**Category II** : **Firm competencies:** innovations, innovative skills, technology, license, intellectual property, rights, rights to patents, copyrights, trademarks, brands, hallmarks, service marks, technical competence, other forms of abilities, etc. Tokens under this category may include physical capital resources, human capital resources, organizational capital resources, production/maintenance resources, administrative resources, or organizational learning resources and strategic vision resources.In alignment with the resource based view (RBV), profits for firms within one industry differs from profits from another due to differing internal capabilities and barriers to resource acquisition and imitation. Peteraf (1993) posits that profits for firms within one industry differs from another due to heterogeneity and isolating mechanisms. Tokens under this category either fall under innovation or unique resources. Innovation allows firms to be equipped with resources that are non-imitable or non-substitutable.

_Table 2. Key Tokens and Associated Bigrams identifying phrases in the &quot;Firm decision making&quot; segment of the dictionaries._

| **Key Unigram Token and Associated Bigrams** | **Dictionary Token Frequency** |
| --- | --- |
| Patent |
 |
| Innovation |
 |
| Brand |
 |
| Develop |
 |

**Category III: Firm actions**** :** such as M&amp;A activities, partnerships, and investment undertaken, etc. There has been abundant research examining the implications of M&amp;A news announcements on share price. Eckbo (2014) shows that merger announcements typically involve a large premium over existing prices (between 40%-50% on average), and lead to a large and rapid change in market prices suggesting that the announcement is news to the market. Routledge et al. (2013) uses a large sample and a regularized logistics regression model to predict merger targets and acquirers from MD&amp;As. Yet, few studies looked into the implications of M&amp;A on sector specific factors, such as the sector specific effects of M&amp;A on long run performance.

_Table 3. Key Tokens and Associated Bigrams identifying phrases in the &quot;Firm actions&quot; segment of the dictionaries._

| **Key Unigram Token and Associated Bigrams** | **Dictionary Token Frequency** |
| --- | --- |
| Acquisition |
 |
| Merger |
 |
| Consolidation |
 |
| Investment |
 |

**Category IV: Results/Inference from firm actions:** such asfees/costs revenue originating from firms&#39; actions (eg. distribution fees, margin ratios). There may be overlaps between tokens that fall under this category and tokens in the performance dictionary, &quot;advertising budget&quot; is an example that is both internal and falls under our positive performance dictionary.

_Table 4. Key Tokens and Associated Bigrams identifying phrases in the &quot;Firm decision making&quot; segment of the dictionaries._

| **Key Unigram Token and Associated Bigrams** | **Dictionary Token Frequency** |
| --- | --- |
| Lease |
 |
| Operate |
 |
| Enter |
 |
| Expand |
 |

Phrases in our **external dictionary** are defined to fall under any one or more of the following categories.

**Category I: Porters&#39; 5 Forces**** :** Analysis of the competition faced by the business, such as competitive rivalry, supplier power, buyer power, threat of substitution and threat of new entry, etc.

| **Key Unigram Token and Associated Bigrams** | **Dictionary Token Frequency** |
| --- | --- |
| Supplier |
 |
| Aggressive |
 |
| Brand |
 |
| Develop |
 |

**Category II: Institutional or Regulatory Factors and Economic factors:** Geopolitical tensions in recent elections, governmental legislations, lawsuits, exchange rates, taxes, risk, foreign currency, fluctuations, interest rates, foreign currency, forward, option, forward position, option position, other shocks such as natural disasters, adverse weather conditions, cyber security threats, terrorism, etc.

| **Key Unigram Token and Associated Bigrams** | **Dictionary Token Frequency** |
| --- | --- |
| Fluctuation |
 |
| Market |
 |
| Law |
 |
| Libor |
 |

Consider the following paragraph for an example of how our system of classification differs from that of the Loughran and McDonald dictionary.

![](RackMultipart20201220-4-1xcaf2u_html_b59fde74d50f4a6a.png)

Whilst the Loughran and McDonald dictionary identifies the blue tokens that either connote positive or negative meaning, our dictionary, in addition, identifies tokens that fall under the performance vocabulary categories (in red) and internal/external categories (in green).

There may be overlaps between the Loughran and McDonald dictionary and our dictionaries. For instance, a sentiment word in the LM dictionary can be referring to a performance token (eg. &quot;negatively affecting revenue&quot;). This will be taken into account as a part of our performance dictionary, however, sentiments that are not associated with the company&#39;s own performance (eg. negative perceptions of retailers and shoppers) is not assessed by the output of our performance dictionary.

**5.** _ **Search Algorithm Design** _

We provide a simple search algorithm example and associated empirical results to show how our dictionary can be used in a bag of words manner. Similar to Loughran and McDonald (2011), our dictionary can be used to compute a performance word count. For our performance words count, we take into account the length of the phrase captured and the length of the document. We also compute a sentence level attribution metric. Each sentence in our corpus will be classified according to whether it contains a positive/negative performance token and an internal/external token.

**Baseline model**

A positive/negative performance token is formed by::

1. An amplifier/negator
2. A unigram or a bigram in either of the pos/neg category in our performance dictionaries

We may have as a resulting performance phrase from aggregating a positive/negative performance token and a performance token. We also include other permutations of the phrase in our dictionary match for all possible inflections of the 2 words in the phrase. For example, consider the resulting performance phrase from variations of the forms of the word &quot;increase&quot; and the performance token &quot;property amortisation&quot;.

![](RackMultipart20201220-4-1xcaf2u_html_925771d8da7fd4b8.png)

Consider the arrangements of these permutations in the form of a nested hashmap: which enables us to compare word by word.

![](RackMultipart20201220-4-1xcaf2u_html_28126f8f4ae506d6.png)

As &quot;property amortisation&quot; is a bigram, we show an example of how a unigram may be stored. The combination of &quot;increase revenue&quot; may be stored in the following way:

![](RackMultipart20201220-4-1xcaf2u_html_60d6ef573d73b36a.png)

The word identification process works in the following manner. We first tokenize the document by sentence, and convert the tokenized sentence into type list. We loop through the token entries in our sentence, if the token appears in the keys (layer 1), we check if the restricted window of the next 1 to 3 words contains a word in keys (layer 2), if so, we check if the restricted window of the next 1 to 3 words contains a word in keys (layer 3). If all layers are matched or there is a blank string in the final key layer, we terminate search and return the full length of the words list matched.

![](RackMultipart20201220-4-1xcaf2u_html_a9712efac553100d.png)

**Optimisation**

To reduce the space complexity of our algorithm, we instead store amplifiers, negators and bads as 3 separate sets, and tokens under our performance phrase list in a hashmap. Key phrases we are trying to match all take the form &quot;amplifier/negator&quot; + &quot;performance token&quot; or &quot;performance token&quot;+ &quot;amplifier/negator&quot;.

![](RackMultipart20201220-4-1xcaf2u_html_30a5adcbd5644136.png)

Let the length of the sentence be w. We initiate an index at position 0 and increment the index procedurally. For each index we check whether it is in the set of amplifiers/negators/bads or in the layer 1 of the positive or negative performance dictionaries, then we proceed to examine whether the any tokens in the next nested layer of the dictionary appears within the subsequent 1 to 3 words in the sentence, until we finish checking all 3 layers. We ensure that every relevant phrase matches within index position in range [0, w) is considered.

In the case of computing the performance word count, if we were to identify the whole phrase, we move to the next word. For each sentence, we record down the number of positive/negative performance phrases, if the number of positive phrases exceed the number of negative phrases, we record the sentence as a positive sentence, if the number of negative phrases exceed the number of positive phrases, we record the sentence as a negative sentence.

Occasionally there are times that tokens in our performance dictionary and our amplifier/negators set overlap. For example, &quot;tax benefit&quot; is a special case as both &quot;tax&quot; and &quot;tax benefit&quot; are included as a negative, and a positive performance token respectively. However,

We want to additionally note that our search algorithm follows the greedy method.

Otherwise, in the case of outputting the attribution sentence count, we terminate search and move onto the next sentence.

Our internal/external dictionary consists of mainly bigrams and unigrams, and whilst iterating through every word in the sentence, lookup is conducted with reference to the internal/external dictionary as well.

We use a nested hashmap to store the dictionary phrases, our token consists of either 1 or 2 words. We add an element to the hashmap as follows: hashmap[word1].append(word2), where hashmap[word1] is type list. The pseudocode below is modified and implemented for each category in our amplifier/negator/bad, pos/neg performance and int/ext dictionaries (For each word, we conduct lookup in a maximum of 7 dictionaries).

**Algorithm** 1 Pseudocode for polarity prediction ![](RackMultipart20201220-4-1xcaf2u_html_cb55ddb5edd60516.gif)

**Input** : inputText, financial text sentence in type list

Dictionaries

**Output:** Document count

1. increment\_layer\_1=0
2. increment\_layer\_ 2=0
3. index=0
4. **WHILE** increment\_layer\_1+increment\_layer\_ 2\&lt;length of inputText:
5. **FOR** increment\_layer\_1 in range(1,4):
6. **FOR** increment\_layer\_ 2 in range(1,4):
7. **IF** increment+index\&lt;length of inputText:
8. **IF** word at index position in inputText is in dictionaries:
9. **IF** word at (index+increment\_layer\_1) position in inputText is in the next nested layer of dictionaries:
10. **IF** word at (index+increment\_layer\_1+increment\_layer\_ 2) position in inputText is in the next nested layer of dictionaries:
11. **DO** accumulate the score for each class in result, conditionally terminate search
12. **ELIF** the next nested layer of dictionaries is empty:
13. **DO** accumulate the score for each class in result, conditionally terminate search
14. **ELIF** the next nested layer of dictionaries is empty:
15. **DO** line 11-12, conditionally terminate search

**4.3 Construction of Global Topics**

Some of the categories constructed with LDA relate to the sector/industry of the business. This may seem to overlap with categories under the Fama French industry portfolios. However, GIC sectors/ Fama French industries do not capture all information delivered by textual description. Whilst GIC sectors ascribe information about the firm, topics drawn from LDA reveals further characteristics about the discussion. For example, consider two firms operating in the pharmaceutical industry. It thus may lead to further analysis into the direction of sentiment attribution in these individual segments.

I subsequently conduct regression analysis to observe the extracted topics from MD&amp;A to their average stock market reaction. I use the dictionaries to analyze changes in the content of MD&amp;A overtime and its implications on stock market performance. (WIP)

**4. 2 LDA**

- **Statistical Document Model**

First consider a document model of the following form:

- Words are represented using unit-based vectors that have a single component equal to 1 and all other components equal to 0. As a result, the vth word in the vocabulary is represented by and for .
- A document is a sequence of N words denoted by )
- A corpus is formed by a collection of M documents: }

**Latent Dirichlet Allocation**

LDA is a generative probabilistic model (Blei, 2012). The underlying assumption of LDA is that it assumes that every document contains a mixture of hidden (latent) topics. Over a distribution of topics, we can infer a topic (and assign a document to it) by choosing the topic that has the highest probability given by a set of words (Blei, Ng, &amp; Jordan, 2003; Blei, 2012).

(i) High Level Summary

LDA assumes that every document will share the same set of topics but exhibit topics in different proportions. A document consists of N word positions, we first populate the word positions with the topic from which the word will come from. We then examine the probability mass function from which the word is drawn, and select a word from the topic we picked.

(ii) Model of LDA

![](RackMultipart20201220-4-1xcaf2u_html_25f6a16ce0a9c616.png)

Fig. Description of each stage of the sampling process

- 𝛂 is the proportion parameter.
- nd is the observed variable of words
- d is the per-document topic proportions
- d is the per word topic assignment
- βk is topics
- Gamma is topic distribution

A topic, k, denoted by βk , is a probability mass function over the entire vocabulary. A topic proportion for document d, denoted by d, is a probability function (mixture) over topics for document d.

is a k-dimensional dirichlet variable (where the dimensionality is the predefined number of topics we extract from the documents). lies in the (k-1)-simplex, if i ≥0, .

We say that the density function of ~Dir(𝛂). The Dirichlet distribution is given by:

![](RackMultipart20201220-4-1xcaf2u_html_cd757acecdc810b5.png)

The dirichlet distribution is used because it is conjugate to the multinomial distribution and has finite dimensional sufficient statistics.

For each topic k ∈ _{1,...,K},_ we draw a topic proportion βk from a Dirichlet Distribution Dir(𝛂). , the K-th dimensional probability vector the dirichlet distribution yields, goes into a multinomial distribution. varies with alpha, when alpha is 1, the probability of each outcome is equally likely. As we vary the parameter alpha, we arrive at different points where the multinomial will land.

![](RackMultipart20201220-4-1xcaf2u_html_c2c50b1cb40980aa.png)

Fig. Dirichlet distribution visualization on a 3-Simplex versus multinomial distributions

The multinomial distribution is a generalization of the binomial function. That is, for n independent trials, each trial is placed into exactly 1 of k categories. The multinomial distribution models the probability of n independent trials each of which leads to a success for exactly one of k categories.

![](RackMultipart20201220-4-1xcaf2u_html_737a46d4a809f5e2.png)

Then, for each document d ∈ _{1,...,M},_ we draw a multinomial distribution from a dirichlet distribution with parameter .

Subsequently, for each word position, n ∈ _{1,...,N},_ we select a hidden topic zn from the topic proportion for the document using the multinomial distribution from the previous step.

Then, for the word position n, we select a word from the corresponding topic βzn, using the topic selected in the previous step.

Hence, the joint likelihood expression is given by:

![](RackMultipart20201220-4-1xcaf2u_html_d96c58a8a534567e.png)
