import requests
import json

url = "https://www.booking.com/dml/graphql?ss=Hyderabad&ssne=Hyderabad&ssne_untouched=Hyderabad&efdco=1&label=gen000nr-10CAMobEIJaHlkZXJhYmFkSAlYBGhQiAEBmAEzuAEFyAEe2AED6AEB-AEBiAIBqAIBuAK17rvBBsACAdICJGQxYmY4ZWE1LTExYzQtNDQ5YS1iNDVjLTkxNjQzM2QyMWZkYdgCAeACAQ&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=city&dest_id=-2097701&dest_type=city&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&sb_lp=1"

payload = json.dumps({
  "operationName": "FullSearch",
  "variables": {
    "includeBundle": False,
    "input": {
      "acidCarouselContext": None,
      "childrenAges": [],
      "doAvailabilityCheck": False,
      "encodedAutocompleteMeta": None,
      "enableCampaigns": True,
      "filters": {},
      "flexibleDatesConfig": {
        "broadDatesCalendar": {
          "checkinMonths": [],
          "los": [],
          "startWeekdays": []
        },
        "dateFlexUseCase": "DATE_RANGE",
        "dateRangeCalendar": {
          "checkin": [],
          "checkout": []
        }
      },
      "forcedBlocks": None,
      "location": {
        "searchString": "Hyderabad",
        "destType": "CITY",
        "destId": -2097701
      },
      "metaContext": {
        "metaCampaignId": 0,
        "externalTotalPrice": None,
        "feedPrice": None,
        "hotelCenterAccountId": None,
        "rateRuleId": None,
        "dragongateTraceId": None,
        "pricingProductsTag": None
      },
      "nbRooms": 1,
      "nbAdults": 2,
      "nbChildren": 0,
      "showAparthotelAsHotel": True,
      "needsRoomsMatch": False,
      "optionalFeatures": {
        "forceArpExperiments": True,
        "testProperties": False
      },
      "pagination": {
        "rowsPerPage": 100,
        "offset": 0
      },
      "rawQueryForSession": "/searchresults.en-gb.html?label=gen000nr-10CAMobEIJaHlkZXJhYmFkSAlYBGhQiAEBmAEzuAEFyAEe2AED6AEB-AEBiAIBqAIBuAK17rvBBsACAdICJGQxYmY4ZWE1LTExYzQtNDQ5YS1iNDVjLTkxNjQzM2QyMWZkYdgCAeACAQ&aid=304142&ss=Hyderabad&ssne=Hyderabad&ssne_untouched=Hyderabad&efdco=1&lang=en-gb&sb=1&src_elem=sb&src=city&dest_id=-2097701&dest_type=city&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&sb_lp=1",
      "referrerBlock": {
        "blockName": "searchbox"
      },
      "sbCalendarOpen": True,
      "sorters": {
        "selectedSorter": None,
        "referenceGeoId": None,
        "tripTypeIntentId": None
      },
      "travelPurpose": 2,
      "seoThemeIds": [],
      "useSearchParamsFromSession": True,
      "merchInput": {
        "testCampaignIds": []
      },
      "webSearchContext": {
        "reason": "CLIENT_SIDE_UPDATE",
        "source": "SEARCH_RESULTS",
        "outcome": "SEARCH_RESULTS"
      },
      "clientSideRequestId": "232748b04af30956"
    },
    "carouselLowCodeExp": False
  },
  "extensions": {},
  "query" : "query FullSearch($input: SearchQueryInput!, $carouselLowCodeExp: Boolean!, $includeBundle: Boolean = false) {\n  searchQueries {\n    search(input: $input) {\n      ...FullSearchFragment\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment FullSearchFragment on SearchQueryOutput {\n  banners {\n    ...Banner\n    __typename\n  }\n  breadcrumbs {\n    ... on SearchResultsBreadcrumb {\n      ...SearchResultsBreadcrumb\n      __typename\n    }\n    ... on LandingPageBreadcrumb {\n      ...LandingPageBreadcrumb\n      __typename\n    }\n    __typename\n  }\n  carousels {\n    ...Carousel\n    __typename\n  }\n  destinationLocation {\n    ...DestinationLocation\n    __typename\n  }\n  entireHomesSearchEnabled\n  dateFlexibilityOptions {\n    enabled\n    __typename\n  }\n  flexibleDatesConfig {\n    broadDatesCalendar {\n      checkinMonths\n      los\n      startWeekdays\n      losType\n      __typename\n    }\n    dateFlexUseCase\n    dateRangeCalendar {\n      flexWindow\n      checkin\n      checkout\n      __typename\n    }\n    __typename\n  }\n  filters {\n    ...FilterData\n    __typename\n  }\n  filtersTrackOnView {\n    type\n    experimentHash\n    value\n    __typename\n  }\n  appliedFilterOptions {\n    ...FilterOption\n    __typename\n  }\n  recommendedFilterOptions {\n    ...FilterOption\n    __typename\n  }\n  pagination {\n    nbResultsPerPage\n    nbResultsTotal\n    __typename\n  }\n  tripTypes {\n    ...TripTypesData\n    __typename\n  }\n  results {\n    ...BasicPropertyData\n    ...MatchingUnitConfigurations\n    ...PropertyBlocks\n    ...BookerExperienceData\n    ...TopPhotos\n    generatedPropertyTitle\n    priceDisplayInfoIrene {\n      ...PriceDisplayInfoIrene\n      __typename\n    }\n    licenseDetails {\n      nextToHotelName\n      __typename\n    }\n    isTpiExclusiveProperty\n    propertyCribsAvailabilityLabel\n    mlBookingHomeTags\n    trackOnView {\n      experimentTag\n      __typename\n    }\n    __typename\n  }\n  searchMeta {\n    ...SearchMetadata\n    __typename\n  }\n  sorters {\n    option {\n      ...SorterFields\n      __typename\n    }\n    __typename\n  }\n  zeroResultsSection {\n    ...ZeroResultsSection\n    __typename\n  }\n  rocketmilesSearchUuid\n  previousSearches {\n    ...PreviousSearches\n    __typename\n  }\n  merchComponents {\n    ...MerchRegionIrene\n    __typename\n  }\n  wishlistData {\n    numProperties\n    __typename\n  }\n  seoThemes {\n    id\n    caption\n    __typename\n  }\n  gridViewPreference\n  advancedSearchWidget {\n    title\n    legalDisclaimer\n    description\n    placeholder\n    ctaText\n    helperText\n    __typename\n  }\n  visualFiltersGroups {\n    ...VisualFiltersGroup\n    __typename\n  }\n  __typename\n}\n\nfragment BasicPropertyData on SearchResultProperty {\n  acceptsWalletCredit\n  basicPropertyData {\n    accommodationTypeId\n    id\n    isTestProperty\n    location {\n      address\n      city\n      countryCode\n      __typename\n    }\n    pageName\n    ufi\n    photos {\n      main {\n        highResUrl {\n          relativeUrl\n          __typename\n        }\n        lowResUrl {\n          relativeUrl\n          __typename\n        }\n        highResJpegUrl {\n          relativeUrl\n          __typename\n        }\n        lowResJpegUrl {\n          relativeUrl\n          __typename\n        }\n        tags {\n          id\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    reviewScore: reviews {\n      score: totalScore\n      reviewCount: reviewsCount\n      totalScoreTextTag {\n        translation\n        __typename\n      }\n      showScore\n      secondaryScore\n      secondaryTextTag {\n        translation\n        __typename\n      }\n      showSecondaryScore\n      __typename\n    }\n    externalReviewScore: externalReviews {\n      score: totalScore\n      reviewCount: reviewsCount\n      showScore\n      totalScoreTextTag {\n        translation\n        __typename\n      }\n      __typename\n    }\n    starRating {\n      value\n      symbol\n      caption {\n        translation\n        __typename\n      }\n      tocLink {\n        translation\n        __typename\n      }\n      showAdditionalInfoIcon\n      __typename\n    }\n    isClosed\n    paymentConfig {\n      installments {\n        minPriceFormatted\n        maxAcceptCount\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  badges {\n    caption {\n      translation\n      __typename\n    }\n    closedFacilities {\n      startDate\n      endDate\n      __typename\n    }\n    __typename\n  }\n  customBadges {\n    showSkiToDoor\n    showBhTravelCreditBadge\n    showOnlineCheckinBadge\n    __typename\n  }\n  description {\n    text\n    __typename\n  }\n  displayName {\n    text\n    translationTag {\n      translation\n      __typename\n    }\n    __typename\n  }\n  geniusInfo {\n    benefitsCommunication {\n      header {\n        title\n        __typename\n      }\n      items {\n        title\n        __typename\n      }\n      __typename\n    }\n    geniusBenefits\n    geniusBenefitsData {\n      hotelCardHasFreeBreakfast\n      hotelCardHasFreeRoomUpgrade\n      sortedBenefits\n      __typename\n    }\n    showGeniusRateBadge\n    __typename\n  }\n  location {\n    displayLocation\n    mainDistance\n    mainDistanceDescription\n    publicTransportDistanceDescription\n    skiLiftDistance\n    beachDistance\n    nearbyBeachNames\n    beachWalkingTime\n    geoDistanceMeters\n    isCentrallyLocated\n    isWithinBestLocationScoreArea\n    popularFreeDistrictName\n    nearbyUsNaturalParkText\n    __typename\n  }\n  mealPlanIncluded {\n    mealPlanType\n    text\n    __typename\n  }\n  persuasion {\n    autoextended\n    geniusRateAvailable\n    highlighted\n    preferred\n    preferredPlus\n    showNativeAdLabel\n    nativeAdId\n    nativeAdsCpc\n    nativeAdsTracking\n    sponsoredAdsData {\n      isDsaCompliant\n      legalEntityName\n      sponsoredAdsDesign\n      __typename\n    }\n    __typename\n  }\n  policies {\n    showFreeCancellation\n    showNoPrepayment\n    showPetsAllowedForFree\n    enableJapaneseUsersSpecialCase\n    __typename\n  }\n  ribbon {\n    ribbonType\n    text\n    __typename\n  }\n  recommendedDate {\n    checkin\n    checkout\n    lengthOfStay\n    __typename\n  }\n  showGeniusLoginMessage\n  hostTraderLabel\n  soldOutInfo {\n    isSoldOut\n    messages {\n      text\n      __typename\n    }\n    alternativeDatesMessages {\n      text\n      __typename\n    }\n    __typename\n  }\n  nbWishlists\n  nonMatchingFlexibleFilterOptions {\n    label\n    __typename\n  }\n  visibilityBoosterEnabled\n  showAdLabel\n  isNewlyOpened\n  propertySustainability {\n    isSustainable\n    certifications {\n      name\n      __typename\n    }\n    __typename\n  }\n  seoThemes {\n    caption\n    __typename\n  }\n  relocationMode {\n    distanceToCityCenterKm\n    distanceToCityCenterMiles\n    distanceToOriginalHotelKm\n    distanceToOriginalHotelMiles\n    phoneNumber\n    __typename\n  }\n  bundleRatesAvailable\n  __typename\n}\n\nfragment Banner on Banner {\n  name\n  type\n  isDismissible\n  showAfterDismissedDuration\n  position\n  requestAlternativeDates\n  merchId\n  title {\n    text\n    __typename\n  }\n  imageUrl\n  paragraphs {\n    text\n    __typename\n  }\n  metadata {\n    key\n    value\n    __typename\n  }\n  pendingReviewInfo {\n    propertyPhoto {\n      lowResUrl {\n        relativeUrl\n        __typename\n      }\n      lowResJpegUrl {\n        relativeUrl\n        __typename\n      }\n      __typename\n    }\n    propertyName\n    urlAccessCode\n    __typename\n  }\n  nbDeals\n  primaryAction {\n    text {\n      text\n      __typename\n    }\n    action {\n      name\n      context {\n        key\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  secondaryAction {\n    text {\n      text\n      __typename\n    }\n    action {\n      name\n      context {\n        key\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  iconName\n  flexibleFilterOptions {\n    optionId\n    filterName\n    __typename\n  }\n  trackOnView {\n    type\n    experimentHash\n    value\n    __typename\n  }\n  dateFlexQueryOptions {\n    text {\n      text\n      __typename\n    }\n    action {\n      name\n      context {\n        key\n        value\n        __typename\n      }\n      __typename\n    }\n    isApplied\n    __typename\n  }\n  __typename\n}\n\nfragment Carousel on Carousel {\n  aggregatedCountsByFilterId\n  carouselId\n  position\n  contentType\n  hotelId\n  name\n  soldoutProperties\n  priority\n  themeId\n  title {\n    text\n    __typename\n  }\n  slides {\n    captionText {\n      text\n      __typename\n    }\n    name\n    photoUrl\n    subtitle {\n      text\n      __typename\n    }\n    type\n    title {\n      text\n      __typename\n    }\n    action {\n      context {\n        key\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment DestinationLocation on DestinationLocation {\n  name {\n    text\n    __typename\n  }\n  inName {\n    text\n    __typename\n  }\n  countryCode\n  ufi\n  __typename\n}\n\nfragment FilterData on Filter {\n  trackOnView {\n    type\n    experimentHash\n    value\n    __typename\n  }\n  trackOnClick {\n    type\n    experimentHash\n    value\n    __typename\n  }\n  name\n  field\n  category\n  filterStyle\n  title {\n    text\n    translationTag {\n      translation\n      __typename\n    }\n    __typename\n  }\n  subtitle\n  options {\n    parentId\n    genericId\n    trackOnView {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClick {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnSelect {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnDeSelect {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnViewPopular {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClickPopular {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnSelectPopular {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnDeSelectPopular {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    ...FilterOption\n    __typename\n  }\n  filterLayout {\n    isCollapsable\n    collapsedCount\n    __typename\n  }\n  stepperOptions {\n    min\n    max\n    default\n    selected\n    title {\n      text\n      translationTag {\n        translation\n        __typename\n      }\n      __typename\n    }\n    field\n    labels {\n      text\n      translationTag {\n        translation\n        __typename\n      }\n      __typename\n    }\n    trackOnView {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClick {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnSelect {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnDeSelect {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClickDecrease {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClickIncrease {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnDecrease {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnIncrease {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    __typename\n  }\n  sliderOptions {\n    min\n    max\n    minSelected\n    maxSelected\n    minPriceStep\n    minSelectedFormatted\n    currency\n    histogram\n    selectedRange {\n      translation\n      __typename\n    }\n    __typename\n  }\n  sliderOptionsPerStay {\n    min\n    max\n    minSelected\n    maxSelected\n    minPriceStep\n    minSelectedFormatted\n    currency\n    histogram\n    selectedRange {\n      translation\n      __typename\n    }\n    __typename\n  }\n  distanceToPoiData {\n    options {\n      text\n      value\n      isDefault\n      __typename\n    }\n    poiNotFound\n    poiPlaceholder\n    poiHelper\n    isSelected\n    selectedOptionValue\n    selectedPlaceId {\n      numValue\n      stringValue\n      __typename\n    }\n    selectedPoiType {\n      destType\n      source\n      __typename\n    }\n    selectedPoiText\n    selectedPoiLatitude\n    selectedPoiLongitude\n    __typename\n  }\n  __typename\n}\n\nfragment FilterOption on Option {\n  optionId: id\n  count\n  selected\n  urlId\n  source\n  field\n  additionalLabel {\n    text\n    translationTag {\n      translation\n      __typename\n    }\n    __typename\n  }\n  value {\n    text\n    translationTag {\n      translation\n      __typename\n    }\n    __typename\n  }\n  starRating {\n    value\n    symbol\n    caption {\n      translation\n      __typename\n    }\n    showAdditionalInfoIcon\n    __typename\n  }\n  __typename\n}\n\nfragment LandingPageBreadcrumb on LandingPageBreadcrumb {\n  destType\n  name\n  urlParts\n  __typename\n}\n\nfragment MatchingUnitConfigurations on SearchResultProperty {\n  matchingUnitConfigurations {\n    commonConfiguration {\n      name\n      unitId\n      bedConfigurations {\n        beds {\n          count\n          type\n          __typename\n        }\n        nbAllBeds\n        __typename\n      }\n      nbAllBeds\n      nbBathrooms\n      nbBedrooms\n      nbKitchens\n      nbLivingrooms\n      nbUnits\n      unitTypeNames {\n        translation\n        __typename\n      }\n      localizedArea {\n        localizedArea\n        unit\n        __typename\n      }\n      __typename\n    }\n    unitConfigurations {\n      name\n      unitId\n      bedConfigurations {\n        beds {\n          count\n          type\n          __typename\n        }\n        nbAllBeds\n        __typename\n      }\n      apartmentRooms {\n        config {\n          roomId: id\n          roomType\n          bedTypeId\n          bedCount: count\n          __typename\n        }\n        roomName: tag {\n          tag\n          translation\n          __typename\n        }\n        __typename\n      }\n      nbAllBeds\n      nbBathrooms\n      nbBedrooms\n      nbKitchens\n      nbLivingrooms\n      nbUnits\n      unitTypeNames {\n        translation\n        __typename\n      }\n      localizedArea {\n        localizedArea\n        unit\n        __typename\n      }\n      unitTypeId\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PropertyBlocks on SearchResultProperty {\n  blocks {\n    blockId {\n      roomId\n      occupancy\n      policyGroupId\n      packageId\n      mealPlanId\n      bundleId\n      __typename\n    }\n    finalPrice {\n      amount\n      currency\n      __typename\n    }\n    originalPrice {\n      amount\n      currency\n      __typename\n    }\n    onlyXLeftMessage {\n      tag\n      variables {\n        key\n        value\n        __typename\n      }\n      translation\n      __typename\n    }\n    freeCancellationUntil\n    hasCrib\n    blockMatchTags {\n      childStaysForFree\n      freeStayChildrenAges\n      __typename\n    }\n    thirdPartyInventoryContext {\n      isTpiBlock\n      __typename\n    }\n    bundle @include(if: $includeBundle) {\n      highlightedText\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PriceDisplayInfoIrene on PriceDisplayInfoIrene {\n  badges {\n    name {\n      translation\n      __typename\n    }\n    tooltip {\n      translation\n      __typename\n    }\n    style\n    identifier\n    __typename\n  }\n  chargesInfo {\n    translation\n    __typename\n  }\n  displayPrice {\n    copy {\n      translation\n      __typename\n    }\n    amountPerStay {\n      amount\n      amountRounded\n      amountUnformatted\n      currency\n      __typename\n    }\n    amountPerStayHotelCurr {\n      amount\n      amountRounded\n      amountUnformatted\n      currency\n      __typename\n    }\n    __typename\n  }\n  averagePricePerNight {\n    amount\n    amountRounded\n    amountUnformatted\n    currency\n    __typename\n  }\n  priceBeforeDiscount {\n    copy {\n      translation\n      __typename\n    }\n    amountPerStay {\n      amount\n      amountRounded\n      amountUnformatted\n      currency\n      __typename\n    }\n    __typename\n  }\n  rewards {\n    rewardsList {\n      termsAndConditions\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      breakdown {\n        productType\n        amountPerStay {\n          amount\n          amountRounded\n          amountUnformatted\n          currency\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    rewardsAggregated {\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      copy {\n        translation\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  useRoundedAmount\n  discounts {\n    amount {\n      amount\n      amountRounded\n      amountUnformatted\n      currency\n      __typename\n    }\n    name {\n      translation\n      __typename\n    }\n    description {\n      translation\n      __typename\n    }\n    itemType\n    productId\n    __typename\n  }\n  excludedCharges {\n    excludeChargesAggregated {\n      copy {\n        translation\n        __typename\n      }\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      __typename\n    }\n    excludeChargesList {\n      chargeMode\n      chargeInclusion\n      chargeType\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  taxExceptions {\n    shortDescription {\n      translation\n      __typename\n    }\n    longDescription {\n      translation\n      __typename\n    }\n    __typename\n  }\n  displayConfig {\n    key\n    value\n    __typename\n  }\n  serverTranslations {\n    key\n    value\n    __typename\n  }\n  __typename\n}\n\nfragment BookerExperienceData on SearchResultProperty {\n  bookerExperienceContentUIComponentProps {\n    ... on BookerExperienceContentLoyaltyBadgeListProps {\n      badges {\n        amount\n        variant\n        key\n        title\n        hidePopover\n        popover\n        tncMessage\n        tncUrl\n        logoSrc\n        logoAlt\n        __typename\n      }\n      __typename\n    }\n    ... on BookerExperienceContentFinancialBadgeProps {\n      paymentMethod\n      backgroundColor\n      hideAccepted\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment TopPhotos on SearchResultProperty {\n  topPhotos {\n    highResUrl {\n      relativeUrl\n      __typename\n    }\n    lowResUrl {\n      relativeUrl\n      __typename\n    }\n    highResJpegUrl {\n      relativeUrl\n      __typename\n    }\n    lowResJpegUrl {\n      relativeUrl\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment SearchMetadata on SearchMeta {\n  availabilityInfo {\n    hasLowAvailability\n    unavailabilityPercent\n    totalAvailableNotAutoextended\n    totalAutoextendedAvailable\n    __typename\n  }\n  boundingBoxes {\n    swLat\n    swLon\n    neLat\n    neLon\n    type\n    __typename\n  }\n  childrenAges\n  dates {\n    checkin\n    checkout\n    lengthOfStayInDays\n    __typename\n  }\n  destId\n  destType\n  guessedLocation {\n    destId\n    destType\n    destName\n    __typename\n  }\n  maxLengthOfStayInDays\n  nbRooms\n  nbAdults\n  nbChildren\n  userHasSelectedFilters\n  customerValueStatus\n  isAffiliateBookingOwned\n  affiliatePartnerChannelId\n  affiliateVerticalType\n  geniusLevel\n  __typename\n}\n\nfragment SearchResultsBreadcrumb on SearchResultsBreadcrumb {\n  destId\n  destType\n  name\n  __typename\n}\n\nfragment SorterFields on SorterOption {\n  type: name\n  captionTranslationTag {\n    translation\n    __typename\n  }\n  tooltipTranslationTag {\n    translation\n    __typename\n  }\n  isSelected: selected\n  __typename\n}\n\nfragment TripTypesData on TripTypes {\n  beach {\n    isBeachUfi\n    isEnabledBeachUfi\n    __typename\n  }\n  ski {\n    isSkiExperience\n    isSkiScaleUfi\n    __typename\n  }\n  __typename\n}\n\nfragment ZeroResultsSection on ZeroResultsSection {\n  title {\n    text\n    __typename\n  }\n  primaryAction {\n    text {\n      text\n      __typename\n    }\n    action {\n      name\n      __typename\n    }\n    __typename\n  }\n  paragraphs {\n    text\n    __typename\n  }\n  type\n  __typename\n}\n\nfragment PreviousSearches on PreviousSearch {\n  childrenAges\n  __typename\n}\n\nfragment MerchRegionIrene on MerchComponentsResultIrene {\n  regions {\n    id\n    components {\n      ... on PromotionalBannerIrene {\n        promotionalBannerCampaignId\n        contentArea {\n          title {\n            ... on PromotionalBannerSimpleTitleIrene {\n              value\n              __typename\n            }\n            __typename\n          }\n          subTitle {\n            ... on PromotionalBannerSimpleSubTitleIrene {\n              value\n              __typename\n            }\n            __typename\n          }\n          caption {\n            ... on PromotionalBannerSimpleCaptionIrene {\n              value\n              __typename\n            }\n            ... on PromotionalBannerCountdownCaptionIrene {\n              campaignEnd\n              __typename\n            }\n            __typename\n          }\n          buttons {\n            variant\n            cta {\n              ariaLabel\n              text\n              targetLanding {\n                ... on OpenContextSheet {\n                  sheet {\n                    ... on WebContextSheet {\n                      title\n                      body {\n                        items {\n                          ... on ContextSheetTextItem {\n                            text\n                            __typename\n                          }\n                          ... on ContextSheetList {\n                            items {\n                              text\n                              __typename\n                            }\n                            __typename\n                          }\n                          __typename\n                        }\n                        __typename\n                      }\n                      buttons {\n                        variant\n                        cta {\n                          text\n                          ariaLabel\n                          targetLanding {\n                            ... on DirectLinkLanding {\n                              urlPath\n                              queryParams {\n                                name\n                                value\n                                __typename\n                              }\n                              __typename\n                            }\n                            ... on LoginLanding {\n                              stub\n                              __typename\n                            }\n                            ... on DeeplinkLanding {\n                              urlPath\n                              queryParams {\n                                name\n                                value\n                                __typename\n                              }\n                              __typename\n                            }\n                            ... on ResolvedLinkLanding {\n                              url\n                              __typename\n                            }\n                            __typename\n                          }\n                          __typename\n                        }\n                        __typename\n                      }\n                      __typename\n                    }\n                    __typename\n                  }\n                  __typename\n                }\n                ... on SearchResultsLandingIrene {\n                  destType\n                  destId\n                  checkin\n                  checkout\n                  nrAdults\n                  nrChildren\n                  childrenAges\n                  nrRooms\n                  filters {\n                    name\n                    value\n                    __typename\n                  }\n                  __typename\n                }\n                ... on DirectLinkLandingIrene {\n                  urlPath\n                  queryParams {\n                    name\n                    value\n                    __typename\n                  }\n                  __typename\n                }\n                ... on LoginLandingIrene {\n                  stub\n                  __typename\n                }\n                ... on DeeplinkLandingIrene {\n                  urlPath\n                  queryParams {\n                    name\n                    value\n                    __typename\n                  }\n                  __typename\n                }\n                ... on SorterLandingIrene {\n                  sorterName\n                  __typename\n                }\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        designVariant {\n          ... on DesktopPromotionalFullBleedImageIrene {\n            image: image {\n              id\n              url(width: 814, height: 138)\n              alt\n              overlayGradient\n              primaryColorHex\n              __typename\n            }\n            colorScheme\n            signature\n            __typename\n          }\n          ... on DesktopPromotionalImageLeftIrene {\n            imageOpt: image {\n              id\n              url(width: 248, height: 248)\n              alt\n              overlayGradient\n              primaryColorHex\n              __typename\n            }\n            colorScheme\n            signature\n            __typename\n          }\n          ... on DesktopPromotionalImageRightIrene {\n            imageOpt: image {\n              id\n              url(width: 248, height: 248)\n              alt\n              overlayGradient\n              primaryColorHex\n              __typename\n            }\n            colorScheme\n            signature\n            __typename\n          }\n          ... on MdotPromotionalFullBleedImageIrene {\n            image: image {\n              id\n              url(width: 358, height: 136)\n              alt\n              overlayGradient\n              primaryColorHex\n              __typename\n            }\n            colorScheme\n            signature\n            __typename\n          }\n          ... on MdotPromotionalImageLeftIrene {\n            imageOpt: image {\n              id\n              url(width: 128, height: 128)\n              alt\n              overlayGradient\n              primaryColorHex\n              __typename\n            }\n            colorScheme\n            signature\n            __typename\n          }\n          ... on MdotPromotionalImageRightIrene {\n            imageOpt: image {\n              id\n              url(width: 128, height: 128)\n              alt\n              overlayGradient\n              primaryColorHex\n              __typename\n            }\n            colorScheme\n            signature\n            __typename\n          }\n          ... on MdotPromotionalImageTopIrene {\n            imageOpt: image {\n              id\n              url(width: 128, height: 128)\n              alt\n              overlayGradient\n              primaryColorHex\n              __typename\n            }\n            colorScheme\n            signature\n            __typename\n          }\n          ... on MdotPromotionalIllustrationLeftIrene {\n            imageOpt: image {\n              id\n              url(width: 200, height: 200)\n              alt\n              overlayGradient\n              primaryColorHex\n              __typename\n            }\n            colorScheme\n            signature\n            __typename\n          }\n          ... on MdotPromotionalIllustrationRightIrene {\n            imageOpt: image {\n              id\n              url(width: 200, height: 200)\n              alt\n              overlayGradient\n              primaryColorHex\n              __typename\n            }\n            colorScheme\n            signature\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      ... on MerchCarouselIrene @include(if: $carouselLowCodeExp) {\n        carouselCampaignId\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment VisualFiltersGroup on VisualFiltersGroup {\n  groupId: id\n  position\n  title {\n    text\n    __typename\n  }\n  visualFilters {\n    title {\n      text\n      __typename\n    }\n    description {\n      text\n      __typename\n    }\n    photoUrl\n    action {\n      name\n      context {\n        key\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"
  })
headers = {
  'Content-Type': 'application/json',
  'accept': '*/*',
  'accept-language': 'en-GB,en-IN;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
   "User-Agent": "PostmanRuntime/7.43.4",
  'Accept-Encoding': 'gzip, deflate, br',
  'Cookie': 'bkng=11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbca8KLfxLPecVouNiV2pbI6YwevMehpARmTT6jp%2FUD5qWrUR8x8kAufP0WnQHCeCHGIyPT%2B0s36DrBjNT6URYPWDiBLJmQFDu4%2BXWbcd%2Fs7GkyidNcObZhsgyOoczQJsRg9qw8fRJv%2Fa6EtMpGIYUAV1nyjmuGAPCT0OYk6uwwDg%3D; bkng_sso_auth=CAIQ0+WGHxpmvsqlQrmMu3fFf4RQ/BL0Nw6DLuUiIfQaT0nSv6uNDlFptSL2/Y/P7qCM2nBCcN4+CV28GDj+ww0wmHcSq+PVZ61BoryUVZrc8SLoyoqnF4dKM1XltCRRLZuBHRjgfjpy+adtAGD6; pcm_consent=analytical%3Dtrue%26countryCode%3DIN%26consentId%3D543e033a-41b8-40dc-98d8-c355cdb50ac9%26consentedAt%3D2025-05-22T10%3A01%3A39.694Z%26expiresAt%3D2025-11-18T10%3A01%3A39.694Z%26implicit%3Dtrue%26marketing%3Dtrue%26regionCode%3DHR%26regulation%3Dnone%26legacyRegulation%3Dnone; pcm_personalization_disabled=0'
}
print(payload)

response = requests.post(url, headers=headers, data=payload)

bed_map = {
    1 : "Single Beds",
    2 : "Double Bed",
    3 : "Extra large Bed",
    4 : "Bunk Bed",
    5 : "Sofa Bed",
    6 : "Large Double Bed",
    7 : "Futton Bed",
    8 : "Double Bunk Bed"
}

hotel_array = []
for hotel in response.json()['data']['searchQueries']['search']['results']:
    try:
        property_name = hotel['displayName']['text']
    except Exception as e:
        print(f"property_name {property_name} exception {e}")
        property_name = ""
    try:
        bed_type = hotel['matchingUnitConfigurations']['unitConfigurations'][0]['bedConfigurations'][0]['beds'][0]['type']
    except Exception as e:
        print(f"property_name {property_name} exception {e} key bed_type")
        bed_type = ""
    try:
        bed_number = hotel['matchingUnitConfigurations']['unitConfigurations'][0]['bedConfigurations'][0]['nbAllBeds']
    except Exception as e:
        print(f"property_name {property_name} exception {e} key bed_number")
        bed_number = ""
    try:
        room_type = hotel['matchingUnitConfigurations']['unitConfigurations'][0]['name']
    except Exception as e:
        print(f"property_name {property_name} exception {e} key room_type")
        room_type = ""
    try:
        price_before_discount = hotel['priceDisplayInfoIrene']['priceBeforeDiscount']['amountPerStay']['amountRounded']
    except Exception as e:
        print(f"property_name {property_name} exception {e} key price_before_discount")
        price_before_discount = ""
    try:
        display_price = hotel['priceDisplayInfoIrene']['displayPrice']['amountPerStay']['amountRounded']
    except Exception as e:
        print(f"property_name {property_name} exception {e} key display_price")
        display_price = ""
    try:
        review_score = hotel['basicPropertyData']['reviewScore']["score"]
    except Exception as e:
        print(f"property_name {property_name} exception {e} key review_score")
        review_score = ""
    try:
        review_count =  hotel['basicPropertyData']['reviewScore']["reviewCount"]
    except Exception as e:
        print(f"property_name {property_name} exception {e} key review_count")
        review_count = ""
    try:
        location = hotel['location']["displayLocation"]
    except Exception as e:
        print(f"property_name {property_name} exception {e} key location")
        location = ""
    try:
        main_distance = hotel['location']["mainDistance"]
    except Exception as e: 
        print(f"property_name {property_name} exception {e} key main_distance")
        main_distance = ""
    try:
        centrally_located = hotel['location']["isCentrallyLocated"]
    except Exception as e:
        print(f"property_name {property_name} exception {e} key centrally_located")
        centrally_located = ""
    try:
        meal_plan = hotel['mealPlanIncluded']['text']
    except Exception as e:
        print(f"property_name {property_name} exception {e} key meal plan")
        meal_plan = ""

    bed_type = bed_map.get(bed_type, '')
    hotel_json = {
        "bed_type" : bed_type,
        "bed_number" : bed_number,
        "room_type" : room_type,
        "price_before_discount" : price_before_discount,
        "meal_plan" : meal_plan,
        "centrally_located" : centrally_located,
        "main_distance" : main_distance,
        "location" : location,
        "review_count" : review_count,
        "review_score" : review_score,
        "property_name" : property_name,
        "display_price" : display_price
    }
    hotel_array.append(hotel_json)


            

import pdb;pdb.set_trace()
