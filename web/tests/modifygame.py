from driver import RetryingDriver

from selenium.webdriver.common.by import By

try:

  # Sign in as an admin
  driver = RetryingDriver("zella")

  # See rules sheet on dashboard
  driver.FindElement([[By.NAME, 'Rules']])

  # See rules page and FAQ page on sidebar
  driver.ExpectContains([[By.NAME, 'playerPagesJoined']], "Rules")
  driver.ExpectContains([[By.NAME, 'playerPagesJoined']], "FAQ")

  # # Go to the Admin dashboard
  driver.Click([[By.NAME, 'Admin Dashboard']])

  # Open up rules, type something.
  driver.FindElement([[By.NAME, 'Rules']])
  driver.Click([[By.TAG_NAME, 'ghvz-desktop-admin-page'], [By.NAME, 'rules-icon'], [By.ID, 'icon']]) 
  driver.SendKeys(
      [[By.NAME, 'admin-page'], [By.TAG_NAME, 'textarea']],
      'rules are cools')

  # If you click Cancel, the new words shouldn't show up.
  driver.Click([[By.NAME, 'admin-page'],[By.ID, 'cancel']])
  driver.DontExpectContains(
      [[By.ID, 'rulesForm']],
      'rules are cools')

  # Open up rules, type something different.
  driver.FindElement([[By.NAME, 'Rules']])
  driver.Click([[By.TAG_NAME, 'ghvz-desktop-admin-page'], [By.NAME, 'rules-icon'], [By.ID, 'icon']]) 
  driver.SendKeys(
      [[By.NAME, 'admin-page'], [By.TAG_NAME, 'textarea']],
      'rules are cools when you save them')

  # If you click Save, the new words should show up.
  driver.Click([[By.NAME, 'admin-page'],[By.ID, 'done']])
  driver.ExpectContains(
      [[By.ID, 'rules']],
      'rules are cools when you save them')

  # Open up Game settings, change each field
  driver.Click([[By.NAME, 'game-icon'], [By.ID, 'icon']])
  driver.SendKeys([[By.ID, 'form-section-game-name'], [By.ID, 'input']], 'A Quick and Certain Death to Humanity')
  driver.SendKeys([[By.ID, 'form-section-game-stunTimer'], [By.TAG_NAME, 'input']], 100)

  # If you click Cancel, the new changes shouldn't show up.
  driver.Click([[By.ID, 'gameForm'],[By.ID, 'cancel']])
  driver.DontExpectContains([[By.NAME, 'game-name']], 'A Quick and Certain Death to Humanity')
  driver.DontExpectContains([[By.NAME, 'game-stunTimer']], "100")

  # # Open up Game settings, change all the fields again.
  driver.Click([[By.NAME, 'game-icon'], [By.ID, 'icon']])
  driver.SendKeys([[By.ID, 'form-section-game-name'], [By.ID, 'input']], 'Welcome to the Zombies-Have-Hunger Games')
  driver.SendKeys([[By.ID, 'form-section-game-stunTimer'], [By.TAG_NAME, 'input']], 42)

  # # If you click Save, the new stun timer should show up.
  driver.Click([[By.ID, 'gameForm'],[By.ID, 'done']])
  driver.ExpectContains([[By.NAME, 'game-name']], 'Welcome to the Zombies-Have-Hunger Games')
  driver.ExpectContains([[By.NAME, 'game-stunTimer']], "42")

  # Go to the FAQ page
  driver.Click([[By.NAME, 'FAQ']])

  # TODO: Add in FAQ change when it has been implemented.

  # Sign in as every user type, make sure all can see rules on dashboard + have rules page
  players = ['deckerd', 'moldavi', 'drake', 'zeke', 'jack','zella']
  for player in players:
    driver.SwitchUser("jack")
    driver.ExpectContains([[By.ID, 'rulesForm']], 'rules are cools when you save them')
    driver.Click([[By.NAME, 'Rules']])

finally:
  # driver.Quit()
  pass
